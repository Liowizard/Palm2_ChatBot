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
        response = palm.generate_text(
            prompt=input_msg, temperature=0.8, candidate_count=1
        )
        print("Working")
        if response.candidates:
            return response.candidates[0]["output"]
    else:
        return response.last
