from os import getenv

from flask import Flask

from api.v1.views import app_views
from models import storage


def create_app():
    """
    Factory for the application

    Returns:
        Instance of flask app
    """

    app = Flask(__name__)
    app.register_blueprint(app_views)
    return app


app = create_app()


@app.teardown_appcontext
def purge_session(req):
    """Remove/close a session at end of request"""
    storage.close()


if __name__ == "__main__":
    host = getenv("CYCLIFE_HOST", "0.0.0.0")
    port = getenv("CYCLIFE_PORT", "5000")
    app.run(host=host, port=port, debug=True, threaded=True)
