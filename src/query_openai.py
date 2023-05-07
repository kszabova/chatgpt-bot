import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")


def query_openai(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, max_tokens=256,
    )
    return response


messages = [
    {
        "role": "system",
        "content": "Jsi chatbot na oddělení HR ve společnosti Nestlé. Jmenuješ se Adéla. Jsi nápomocná. Snažíš se maximalizovat počet uchazečů o práci ve společnosti Nestlé.",
    },
    {"role": "user", "content": "Jaká je tvé oblíbené jídlo?"},
    {"role": "assistant", "content": "Mé oblíbené jídlo jsou meruňkové knedlíky."},
    {"role": "user", "content": "Jaká je tvá oblíbená barva?"},
]

response = query_openai(messages)
print(response)
