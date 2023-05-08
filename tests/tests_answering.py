from src.query_openai import query_openai
from src.prompt_constructor import PromptConstructor


def test_answer_personality_color():
    sentence = "Jaká je tvoje oblíbená barva?"
    messages = PromptConstructor.get_bot_personality_answer_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_answer_personality_food():
    sentence = "Jaká je tvoje oblíbené jídlo?"
    messages = PromptConstructor.get_bot_personality_answer_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_answer_personality_fear():
    sentence = "Z čeho máš strach?"
    messages = PromptConstructor.get_bot_personality_answer_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def run_tests_answering():
    test_answer_personality_color()
    test_answer_personality_food()
    test_answer_personality_fear()


if __name__ == "__main__":
    run_tests_answering()

