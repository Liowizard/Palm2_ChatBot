import os

import google.generativeai as palm
from dotenv import load_dotenv

load_dotenv()

palm.configure(api_key=os.environ["PALM_API_KEY"])


def chat_bot(input="", data="", temperature=0.4):

    print("input_value", input, data, temperature)

    generation_config = {
        "temperature": int(temperature),
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE",
        },
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
    input = str(data) + "\n\n    " + input
    response = model.generate_content(input)
    return response.text


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


palm.configure(api_key=os.environ["PALM_API_KEY"])


defaults = {
    "model": "models/gemini-pro",
    "temperature": 0.4,
    "candidate_count": 1,
    "top_k": 40,
    "top_p": 0.95,
    "max_output_tokens": 1024,
}


def old_chat_bot(input_msg):
    response = palm.chat(messages=input_msg)

    # response = response.reply(input_msg)
    if not response.last:
        response = palm.generate_text(
            prompt=input_msg, temperature=0.8, candidate_count=1
        )
        print("Working")
        if response.candidates:
            return response.candidates[0]["output"]
    else:
        return response.last
