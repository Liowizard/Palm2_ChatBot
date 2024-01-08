import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from Chat_Bot import chat_bot

app = Flask(__name__)


@app.route("/", methods=["POST"])
def hello():
    if request.is_json:
        # Get the JSON data from the request
        data = request.get_json()

        # Get the value of the 'input' key from the JSON data
        input_value = data.get("input", "Hi")

        print("input_value", input_value)

        responce = chat_bot(input_value)

        # Return a JSON response to the client
        return jsonify({"responce": responce})
    else:
        return jsonify({"error": "Invalid JSON data"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
