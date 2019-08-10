"""

[BROKER SERVER]
===================================================

Supposed to run on a different server than the main application.

For local use, the main app (server) runs on port 5000.
This server runs on a different port (say 6000, if available).

"""

from flask import (
    Flask,
    make_response,
    render_template,
    request
)
from flask_cors import CORS
import json
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(11)

# Enable cross-origin requests
CORS(app)
UPLOAD_DIR = "storage/"

if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)


@app.route('/')
def index():
    return json.dumps({
        "msg": "Default response"
    })


# Endpoint for uploading file identified with <file_id>
@app.route('/storage/<file_id>', methods=['POST'])
def storage(file_id):
    if "/" in file_id:
        # Return 400 BAD REQUEST
        bad_resp = make_response("Input contains non-allowed bytes", 400)
        return bad_resp

    with open(os.path.join(UPLOAD_DIR, file_id), 'wb') as fp:
        fp.write(request.data)

    return make_response("", 201)


if __name__ == "__main__":
    app.run(debug=True, port=6000)
