import os

import google.generativeai as palm
from dotenv import load_dotenv
from halo import Halo

load_dotenv()

defaults = {
    "model": "models/gemini-pro",
    "temperature": 0.4,
    "candidate_count": 1,
    "top_k": 40,
    "top_p": 0.95,
    "max_output_tokens": 1024,
}

palm.configure(api_key=os.environ["PALM_API_KEY"])
inpu = 0
while True:
    print("CLAI> ", end="")
    input_msg = input()
    if not input_msg:
        continue
    spinner = Halo(text="Processing...", spinner="dots")
    spinner.start()
    if inpu == 0:
        response = palm.chat(messages=input_msg)
        inpu += 1
    else:
        response = response.reply(input_msg)
    spinner.stop()
    if not response.last:
        response = palm.generate_text(prompt=input_msg, **defaults)
        print(response.result)
        if not response.result:
            print("CLAI> Sorry, I couldn't fetch a response for that.")
            continue
    else:
        print(response.last)
        continue
