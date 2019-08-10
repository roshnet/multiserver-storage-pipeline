from flask import (
    Flask,
    jsonify,
    request
)

app = Flask(__name__)


@app.route('/')
def default():
    return jsonify({
        "status": "default endpoint"
    })


@app.route('/receive', methods=['PUT', 'POST', 'GET'])
def receive():
    if request.method == 'GET':
        return "You sent a GET request to /receive endpoint."

    if request.method == 'PUT':
        return "You sent a PUT request to /receive endpoint."

    return "You sent a POST request to /receive endpoint."


@app.route('/uploader')
def upload_handler():
    return "You just called upload handler"


if __name__ == "__main__":
    app.run(debug=True)
