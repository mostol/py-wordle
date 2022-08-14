# Based on the LING508 Sanskrit example project, https://github.com/jjberry-508/sanskrit-508

from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
from app.services import Services


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/guess": {"origins": "http://localhost:port"}})

services = Services()


@app.route("/guess", methods=["POST"])  # Add URL here, after "/" (e.g. "/guess")
@cross_origin(origin='localhost', headers=['Content-Type', 'Authorization'])
def best_guess():
    data = request.get_json()
    # print(data)
    #
    # services.add_guesses()

    return jsonify(data["word"])


if __name__ == "__main__":
    app.run()
