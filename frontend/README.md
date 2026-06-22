# React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- [@vitejs/plugin-react](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react) uses [Oxc](https://oxc.rs)
- [@vitejs/plugin-react-swc](https://github.com/vitejs/vite-plugin-react/blob/main/packages/plugin-react-swc) uses [SWC](https://swc.rs/)

## React Compiler

The React Compiler is not enabled on this template because of its impact on dev & build performances. To add it, see [this documentation](https://react.dev/learn/react-compiler/installation).

## Expanding the ESLint configuration

If you are developing a production application, we recommend using TypeScript with type-aware lint rules enabled. Check out the [TS template](https://github.com/vitejs/vite/tree/main/packages/create-vite/template-react-ts) for information on how to integrate TypeScript and [`typescript-eslint`](https://typescript-eslint.io) in your project.

## Project Quickstart (project-specific)

Follow these steps from the repository root.

- Create and activate a Python virtual environment (Windows PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

- Install Python dependencies:

```powershell
pip install -r requirements.txt
```

- Run the backend Flask API (serves the steganography endpoints):

```powershell
python app.py
```

- Run the Python test suite:

```powershell
.venv\Scripts\python -m pytest -q
```

- Frontend (from `frontend/`): install deps and run or build:

```bash
cd frontend
npm ci
npm run dev      # development server with HMR
npm run build    # production build -> produces dist/
npm run preview  # serve built dist/ for preview
```

Notes:
- Build output: `frontend/dist/` contains `index.html` and `assets/` (JS/CSS bundles).
- Lint: `npm run lint` (ESLint). Recent unused-import ESLint errors for default `React` imports were fixed.
- Tests: all Python tests pass in this repo (`pytest`).
- Pillow deprecation: code uses `Image.getdata()` which triggers a deprecation warning; consider migrating to `get_flattened_data()` in `core/lsb_encoder.py`, `core/lsb_decoder.py`, and `core/metrics.py`.

If you want, I can add a root `README.md` with the same quickstart, or open a PR with these changes.
