from flask import Flask, request, jsonify

# from app.services import Services


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app
