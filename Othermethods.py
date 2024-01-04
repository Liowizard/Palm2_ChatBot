import os

import google.generativeai as palm
from dotenv import load_dotenv

palm.configure(api_key=os.getenv("PALM_API_KEY"))

# Set up the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = palm.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

chat = model.start_chat(history=[])

history = []


def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response


while True:
    req = input(">")

    response = get_gemini_response(req)

    history.append(("You", req))

    for chunk in response:
        print(chunk.text)
        history.append(("Bot", chunk.text))

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


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


def chat_bot2(input_msg):
    response = palm.chat(messages=input_msg)
    # response = response.reply(input_msg)
    if not response.last:
        # response = palm.generate_text(prompt=input_msg, **defaults)
        # if not response.result:
        return "Hi i am Digival AI and i am here to help with your Educational problems"
    else:
        return response.last


# models = [m for m in palm.list_models()]

# for m in models:
#     print(f"Model Name: {m.name}")


# print(chat_bot("which one is best text-bison-001 or gemini-pro"))


# Model Name: models/chat-bison-001
# Model Name: models/text-bison-001
# Model Name: models/embedding-gecko-001
# Model Name: models/gemini-pro
# Model Name: models/gemini-pro-vision
# Model Name: models/embedding-001
# Model Name: models/aqa


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


import os

import google.generativeai as palm
from dotenv import load_dotenv

load_dotenv()

# import google.generativeai as palm

palm.configure(api_key=os.environ["PALM_API_KEY"])

# Set up the model
generation_config = {
    "temperature": 0.4,
    "candidate_count": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 2048,
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE",
    },
]

model = palm.GenerativeModel(
    model_name="gemini-pro",
    generation_config=generation_config,
    safety_settings=safety_settings,
)

conversation_history = []


def chat_bot(input_msg):
    global conversation_history
    print("conversation_history", conversation_history)

    prompt = " ".join(conversation_history) + " " + input_msg
    response = model.generate_content(prompt)

    conversation_history.append(input_msg)
    conversation_history.append(response.text)

    # print(response.text)
    return response.text


# while True:
#     st = input(">")
#     print(chat_bot(st))
