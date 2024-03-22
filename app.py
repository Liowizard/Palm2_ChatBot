import os

from flask import Flask, jsonify, request
from flask_cors import CORS

from gemini_pro import chat_bot, old_chat_bot

app = Flask(__name__)

CORS(app)


@app.route("/", methods=["POST"])
def hello():
    if request.is_json:
        # Get the JSON data from the request
        data = request.get_json()

        # Get the value of the 'input' key from the JSON data
        input_value = data.get("input")

        print("input_value", input_value)

        responce = old_chat_bot(input_value)

        # Return a JSON response to the client
        return jsonify({"responce": responce})
    else:
        return jsonify({"error": "Invalid JSON data"}), 400


@app.route("/gemini-pro", methods=["POST"])
def New_chat_bot():
    if request.is_json:

        # Get the JSON data from the request
        data = request.get_json()

        if "input" in data:

            print(data)

            defaults = chat_bot.__defaults__

            print("defaults", defaults)

            default_kwargs = {
                "input": defaults[0],
                "data": defaults[1],
                "temperature": defaults[2],
            }

            default_kwargs.update(data)

            responce = chat_bot(**default_kwargs)
        else:
            return jsonify({"responce": "sorry i havent receive a prompt"})
        # responce = chat_bot(prompt, json, temperature)

        # Return a JSON response to the client
        return jsonify({"responce": responce})
    else:
        return jsonify({"error": "Invalid JSON data"}), 400


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
