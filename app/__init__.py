"""ModaLine — мінімальний Flask API для демонстрації версіонування."""
from pathlib import Path
from flask import Flask, jsonify

__version__ = (Path(__file__).resolve().parent.parent / "VERSION").read_text(encoding="utf-8").strip()


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "dev-only-secret"

    from .catalog import bp as catalog_bp
    app.register_blueprint(catalog_bp)
    try:  # модуль auth з'являється у feature/add-login
        from .auth import bp as auth_bp
        app.register_blueprint(auth_bp)
    except ImportError:
        pass

    @app.get("/api/version")
    def version():
        return jsonify(version=__version__)

    return app
