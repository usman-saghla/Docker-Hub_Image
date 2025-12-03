"""Simple Flask application with clear comments for learning.

This file exposes two endpoints:
- `/`       : simple text welcome message
- `/health` : returns a small JSON object to indicate the app is healthy

To run locally for development:
    $ python app.py

In production use a WSGI server such as `gunicorn` (see `DockerFile`).
"""

import os
from flask import Flask, jsonify


def create_app() -> Flask:
    """Application factory — returns a configured Flask app.

    Using an application factory is a good practice even for small apps because
    it makes testing and configuration easier later on.
    """
    app = Flask(__name__)

    @app.route("/")
    def home():
        """Root endpoint that returns a friendly message.

        Returns a plain text response (status 200).
        """
        return "Hello, World!", 200

    @app.route("/health")
    def health():
        """Health-check endpoint.

        Returns a small JSON object. Useful for container orchestration
        or monitoring checks.
        """
        return jsonify({"status": "ok"}), 200

    return app


# Create the app using the factory so tests can import `create_app` if needed.
app = create_app()


if __name__ == "__main__":
    # Use environment variables for configuration so the behavior is easy to
    # change without editing code. We default to host 0.0.0.0 and port 5000.
    host = os.environ.get("FLASK_RUN_HOST", "0.0.0.0")
    port = int(os.environ.get("FLASK_RUN_PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "1") == "1"

    # Start the built-in development server. For production, use gunicorn.
    app.run(host=host, port=port, debug=debug)