import os

import google.generativeai as palm
from dotenv import load_dotenv

load_dotenv()
palm.configure(api_key=os.environ["PALM_API_KEY"])

defaults = {
    "model": "models/gemini-pro",
    "temperature": 0.4,
    "candidate_count": 1,
    "top_k": 40,
    "top_p": 0.95,
    "max_output_tokens": 1024,
}


def chat_bot(input_msg):
    response = palm.chat(messages=input_msg)
    # response = response.reply(input_msg)
    if not response.last:
        response = palm.generate_text(prompt=input_msg, **defaults)
        if not response.result:
            return "CLAI> Sorry, I couldn't fetch a response for that."
    else:
        return response.last


# models = [m for m in palm.list_models()]

# for m in models:
#     print(f"Model Name: {m.name}")


# print(chat_bot("What is your"))


# Model Name: models/chat-bison-001
# Model Name: models/text-bison-001
# Model Name: models/embedding-gecko-001
# Model Name: models/gemini-pro
# Model Name: models/gemini-pro-vision
# Model Name: models/embedding-001
# Model Name: models/aqa
