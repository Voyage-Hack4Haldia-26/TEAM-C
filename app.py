import os
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

app = Flask(__name__)
CORS(app)
BASE = os.path.dirname(os.path.abspath(__file__))


@app.get("/")
def index():
    return send_from_directory(BASE, "index.html")


@app.get("/health")
def health():
    return jsonify(status="ok", project="Team C: Flood Early Warning", stack="flask")

@app.route("/api/readings", methods=["GET"])
def ep_0(**kwargs):
    # TODO: Latest readings per zone
    return jsonify(error="Not implemented", todo="Latest readings per zone"), 501

@app.route("/api/predict", methods=["POST"])
def ep_1(**kwargs):
    # TODO: Body: features -> {risk, score}
    return jsonify(error="Not implemented", todo="Body: features -> {risk, score}"), 501

@app.route("/api/alerts", methods=["GET"])
def ep_2(**kwargs):
    # TODO: Active alerts
    return jsonify(error="Not implemented", todo="Active alerts"), 501


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
