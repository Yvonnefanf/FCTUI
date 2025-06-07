from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS, cross_origin

app = Flask(__name__, static_folder='', static_url_path='')
cors = CORS(app, supports_credentials=True)

@app.route("/", methods=["GET"])
def customize():
    return send_from_directory(app.static_folder, 'index.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8085)
