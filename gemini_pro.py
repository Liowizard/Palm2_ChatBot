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


# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


import base64

import vertexai
import vertexai.preview.generative_models as generative_models
from vertexai.generative_models import FinishReason, GenerativeModel, Part


def vertexai_chat_bot(input="", data="", temperature=0.4):
    vertexai.init(project="staging-408712", location="us-central1")
    model = GenerativeModel("gemini-1.0-pro-002")


    generation_config = {
    "max_output_tokens": 2048,
    "temperature": int(temperature),
    "top_p": 1,
    }


    safety_settings = {
    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
}
    
    # data = """{\"temperature\":0.6,\"data\":\"!!!{\\\"staffName\\\":\\\"Khalid Ahamed\\\",\\\"schedule\\\":[{\\\"startTime\\\":\\\"09:00 AM\\\",\\\"endTime\\\":\\\"10:30 AM\\\",\\\"courseName\\\":\\\"Human Anatomy\\\",\\\"classroom\\\":\\\"Room 101\\\",\\\"topicName\\\":\\\"Introduction to Human Body Systems\\\"},{\\\"startTime\\\":\\\"11:00 AM\\\",\\\"endTime\\\":\\\"12:30 PM\\\",\\\"courseName\\\":\\\"General Pediatrics\\\",\\\"classroom\\\":\\\"Room 102\\\",\\\"topicName\\\":\\\"Childhood Nutrition\\\"},{\\\"startTime\\\":\\\"01:00 PM\\\",\\\"endTime\\\":\\\"02:30 PM\\\",\\\"courseName\\\":\\\"Cardiac Surgery\\\",\\\"classroom\\\":\\\"Room 103\\\",\\\"topicName\\\":\\\"Basics of Cardiac Surgical Procedures\\\"},{\\\"startTime\\\":\\\"03:00 PM\\\",\\\"endTime\\\":\\\"04:30 PM\\\",\\\"courseName\\\":\\\"Shakespearean Literature\\\",\\\"classroom\\\":\\\"Room 201\\\",\\\"topicName\\\":\\\"Analysis of \'Macbeth\'\\\"},{\\\"startTime\\\":\\\"05:00 PM\\\",\\\"endTime\\\":\\\"06:30 PM\\\",\\\"courseName\\\":\\\"Modern Art History\\\",\\\"classroom\\\":\\\"Room 202\\\",\\\"topicName\\\":\\\"Impressionism and Post-Impressionism\\\"},{\\\"startTime\\\":\\\"07:00 PM\\\",\\\"endTime\\\":\\\"08:30 PM\\\",\\\"courseName\\\":\\\"Clinical Pharmacology\\\",\\\"classroom\\\":\\\"Room 104\\\",\\\"topicName\\\":\\\"Drug Interactions and Side Effects\\\"}],\\\"proctoringDuties\\\":[{\\\"date\\\":\\\"2024-04-15\\\",\\\"startTime\\\":\\\"10:00 AM\\\",\\\"endTime\\\":\\\"01:00 PM\\\",\\\"examName\\\":\\\"Finals in Medicine\\\",\\\"examCenter\\\":\\\"Central Hall\\\"},{\\\"date\\\":\\\"2024-04-17\\\",\\\"startTime\\\":\\\"09:00 AM\\\",\\\"endTime\\\":\\\"12:00 PM\\\",\\\"examName\\\":\\\"Midterm in Pediatrics\\\",\\\"examCenter\\\":\\\"North Wing\\\"},{\\\"date\\\":\\\"2024-04-20\\\",\\\"startTime\\\":\\\"02:00 PM\\\",\\\"endTime\\\":\\\"05:00 PM\\\",\\\"examName\\\":\\\"Finals in Pharmacology\\\",\\\"examCenter\\\":\\\"Exam Room 3\\\"}]}!!!\",\"input\":\"based on this data on Schedule  what scheudle on friday  \"} based on this data on Schedule  what duty 
    # on friday"""


    responses = model.generate_content(
      [data +input],
      generation_config=generation_config,
      safety_settings=safety_settings,
      stream=True,
  )
    # print(responses)
    for response in responses:
        # print(response.text, end="")
        # print("--------------------------------")
        yield response.text


# vertexai_chat_bot()

