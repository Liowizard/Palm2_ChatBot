import openai

openai.api_key = "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"

openai
# client.api_key("")
response = openai.completions.create(
    model="gpt-3.5-turbo-instruct",
    prompt="hi",
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
)

print("response", response)
