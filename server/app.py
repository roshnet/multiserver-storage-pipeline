"""

[ROOT SERVER]
===================================================

This is the main application server, some routes
of which are meant to be merged into the existing
application.

This essentially serves as the main interactor
with all front end scripts.

From the point of view of the multi-server API
pipeline, this behaves as the root server.

"""

from flask import (
    Flask,
    request,
    render_template
)
import json
import os
import requests
from werkzeug import secure_filename


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(11)
app.config['UPLOAD_FOLDER'] = "storage"

BROKER_URL = "http://localhost:6000/storage"


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        return "POST"
    return json.dumps({
        "msg": "Default endpoint"
    })


# @app.route('/upload', methods=['GET', 'POST'])
# def upload():
#     if request.method == 'GET':
#         return render_template('upload.html')


@app.route('/to_broker', methods=['GET', 'POST'])
def to_broker():
    """
    Receives data from front end, and passes it on to the broker API.

    Two approaches possible -
        i - Save file here (on this server), and then use that file to send
        the broker (followed by disk deletion to save available storage)
        ii - Pass the file continuously to the broker API

    [Proceeding with the former]

    """
    if request.method == 'GET':
        return render_template('upload.html')


    # [Write uploaded file to disk]
    f = request.files['file']
    f.save(secure_filename(f.filename))

    # [Read file and send to broker]
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], f.filename)
    with open(filepath, 'rb') as fp:
        content = fp.read()

    # Add logic to make <filename> unique
    upload = requests.post(os.path.join(BROKER_URL, f.filename),
                           data=content)

    if upload.status_code > 201:
        # Do something to alert user that upload failed
        return "Upload failed"

    # [Free up disk space]
    if os.path.isfile(filepath):
        os.remove(filepath)
        # DEBUG
        return "File removed, and broker-upload successful"

    # Fetch and return actual status
    return "File not removed, but broker-upload successful"


if __name__ == "__main__":
    app.run(debug=True)
