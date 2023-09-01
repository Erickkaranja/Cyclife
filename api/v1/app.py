from flask import Flask

from api.v1.views import app_views
from models import storage

app = Flask(__name__)
app.register_blueprint(app_views)

print(app.url_map)


@app.teardown_appcontext
def purge_session(req):
    """Remove/close a session at end of request"""
    storage.close()


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
