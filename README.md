# 🔐 StealthVault - Secure Image Steganography Platform

StealthVault is a full-stack image steganography application that securely hides and extracts files within images using **AES-256 encryption** and a **custom Least Significant Bit (LSB)** encoding algorithm. The application combines a React frontend with a Flask backend and is fully containerized using Docker for portable deployment.

---

## ✨ Features

* 🔒 AES-256 encrypted file protection
* 🖼️ Custom LSB-based image steganography
* 📁 Hide and extract files of various types
* 🔑 Password-protected encryption and extraction
* ✅ SHA-256 integrity verification
* 📊 Image quality analysis using PSNR and MSE
* 🌐 React + Flask full-stack architecture
* 🐳 Dockerized for consistent and portable deployment

---

## 🏗️ Architecture

```text
                User
                  │
                  ▼
        React Frontend (Vite)
                  │
                  ▼
          Flask REST API
                  │
      ┌───────────┼───────────┐
      ▼           ▼           ▼
 AES-256     LSB Encoder   SHA-256
 Encryption               Integrity
      │
      ▼
 Stego Image (PNG)
```

---

## 🛠️ Tech Stack

### Frontend

* React
* Vite
* Axios
* CSS

### Backend

* Python
* Flask
* Flask-CORS

### Security & Steganography

* AES-256 Encryption
* SHA-256 Integrity Verification
* Custom LSB Encoding/Decoding
* Pillow (PIL)

### DevOps

* Docker

---

## 📂 Project Structure

```text
StealthVault/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── README.md
│
├── core/
│   ├── aes_crypto.py
│   ├── lsb_encoder.py
│   ├── lsb_decoder.py
│   ├── file_steganography.py
│   ├── integrity.py
│   ├── metrics.py
│   ├── capacity_checker.py
│   └── file_handler.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── uploads/
└── outputs/
```

---

## 🚀 Running with Docker

### Pull the Docker Image

```bash
docker pull podamounitha/stealthvault:latest
```

### Run the Container

```bash
docker run -p 5000:5000 podamounitha/stealthvault:latest
```

Open your browser:

```text
http://localhost:5000
```

---

## 💻 Local Development

### Backend

```bash
pip install -r requirements.txt
python app.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

---

## 🔒 Security Features

* AES-256 encryption for payload confidentiality
* Password-based encryption and decryption
* SHA-256 hash verification to ensure file integrity
* Capacity validation before embedding
* Custom 32-bit payload length header for reliable extraction

---

## 📈 Image Quality Metrics

StealthVault evaluates the impact of steganography on image quality using:

* **PSNR (Peak Signal-to-Noise Ratio)**
* **MSE (Mean Squared Error)**

These metrics help ensure that hidden data introduces minimal visible distortion.

---

## 📸 Screenshots

Add screenshots here after deployment.

```
screenshots/
├── home.png
├── hide-file.png
├── extract-file.png
└── result.png
```

---

## 🎯 Future Enhancements

* Support for audio and video steganography
* Drag-and-drop file uploads
* User authentication
* Cloud deployment
* Advanced steganalysis detection
* Compression before encryption

---

## 👨‍💻 Author

**Poda Mounitha**

---

## 📄 License

This project is released under the MIT License.

---

⭐ If you found this project useful, consider giving the repository a star!
