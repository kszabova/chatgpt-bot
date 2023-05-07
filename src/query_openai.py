import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def query_openai(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, max_tokens=256,
    )
    message = response.get("choices", [{}])[0].get("message", {}).get("content")
    return message

