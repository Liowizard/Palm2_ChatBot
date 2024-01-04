import os

import google.generativeai as palm
from dotenv import load_dotenv

load_dotenv()

# import google.generativeai as palm

palm.configure(api_key=os.environ["PALM_API_KEY"])

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
