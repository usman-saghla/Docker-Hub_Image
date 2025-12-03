## Simple Flask APP

This repository contains a minimal, well-commented Flask application suitable
for learning how to build, test, and containerize a Python web app.

Features:
- A clear `app.py` with an application factory and two endpoints: `/` and `/health`.
- Unit tests using `pytest`.
- A `DockerFile` showing how to build a small production-ready image with `gunicorn`.

### Setup (local development)

1. Create a virtual environment (recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app locally:

```powershell
python app.py
# Open http://localhost:5000 in your browser
```

### Run tests

```powershell
pytest -q
```

### Build and run with Docker

```powershell
docker build -t simple-flask-app -f DockerFile .
docker run -p 5000:5000 simple-flask-app
```

### Notes

- The app uses `gunicorn` in the container for production-like behavior. For
	simple development you can use `python app.py` which runs Flask's dev server.
- Want help adding CI or more features? Ask and I can add GitHub Actions examples.