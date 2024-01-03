import os

from flask import Flask, request

from Chat_Bot import chat_bot

app = Flask(__name__)


@app.route("/")
def hello():
    # Get the value of the 'input' parameter from the URL
    input_value = request.args.get("input", "hii")

    # Print the input value
    print("input_value", input_value)

    responce = chat_bot(input_value)

    # Return a response to the client
    return responce


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
