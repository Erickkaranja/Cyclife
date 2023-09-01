#!/usr/bin/python3
'''implementing a RESTApi blueprint.'''

from models import storage
import os
from flask import Flask
from flask import make_response, jsonify
from flask_cors import CORS
from api.v1.views import app_views

app = Flask(__name__)
cors = CORS(app, resources={"/*": {"origins": os.getenv("CYCLIFE_API_HOST",
            "0.0.0.0")}})
'''flask web application instance.'''
app.register_blueprint(app_views)

@app.teardown_appcontext
def teardown(self):
    '''call the close function from storage.'''
    storage.close()

if __name__ == "__main__":
    host = os.getenv("CYCLIFE_API_HOST", "0.0.0.0")
    port = os.getenv("CYCLIFE_API_PORT")
    app.run(host=host, port=port, threaded=True)
