from flask import Flask
from flask import request
from flask import jsonify
from flask import send_file
from flask import send_from_directory
from flask_cors import CORS

from core.file_steganography import FileSteganography
from core.metrics import ImageMetrics

import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

os.makedirs(
    OUTPUT_FOLDER,
    exist_ok=True
)


@app.route("/")
def home():

    return jsonify(
        {
            "status": "running"
        }
    )


@app.route(
    "/hide-file",
    methods=["POST"]
)
def hide_file():

    image = request.files["image"]
    secret_file = request.files["file"]

    password = request.form["password"]

    image_path = os.path.join(
        UPLOAD_FOLDER,
        image.filename
    )

    secret_path = os.path.join(
        UPLOAD_FOLDER,
        secret_file.filename
    )

    image.save(image_path)

    secret_file.save(secret_path)

    output_path = os.path.join(
        OUTPUT_FOLDER,
        "hidden.png"
    )

    FileSteganography.hide_file(
        image_path=image_path,
        file_path=secret_path,
        password=password,
        output_path=output_path
    )

    mse = ImageMetrics.calculate_mse(
        image_path,
        output_path
    )

    psnr = ImageMetrics.calculate_psnr(
        image_path,
        output_path
    )

    return jsonify(
        {
            "message":
                "File hidden successfully",
            "output_image":
                output_path,
            "mse":
                mse,
            "psnr":
                psnr
        }
    )


@app.route(
    "/extract-file",
    methods=["POST"]
)
def extract_file():

    image = request.files["image"]

    password = request.form["password"]

    image_path = os.path.join(
        UPLOAD_FOLDER,
        image.filename
    )

    image.save(
        image_path
    )

    recovered_file = (
        FileSteganography.extract_file(
            image_path=image_path,
            password=password,
            output_directory=
                OUTPUT_FOLDER
        )
    )

    return send_file(
        recovered_file,
        as_attachment=True
    )


@app.route("/download/<path:filename>")
def download_file(filename):
    return send_from_directory(
        OUTPUT_FOLDER,
        filename,
        as_attachment=True
    )


if __name__ == "__main__":

    app.run(
        debug=True
    )