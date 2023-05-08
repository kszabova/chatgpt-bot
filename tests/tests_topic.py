from src.query_openai import query_openai
from src.prompt_constructor import PromptConstructor


def test_topic_personality_yes():
    sentence = "Jaká je tvoje oblíbená barva?"
    messages = PromptConstructor.get_is_bot_personality_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_topic_personality_no():
    sentence = "Kde je nejbližší kavárna?"
    messages = PromptConstructor.get_is_bot_personality_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_topic_coc_yes():
    sentence = "Můžu zastávat funkci v představenstvu jiné firmy?"
    messages = PromptConstructor.get_is_code_of_conduct_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_topic_coc_no():
    sentence = "Kde je nejbližší kavárna?"
    messages = PromptConstructor.get_is_code_of_conduct_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def run_tests_topic():
    test_topic_personality_yes()
    test_topic_personality_no()
    test_topic_coc_yes()
    test_topic_coc_no()


if __name__ == "__main__":
    run_tests_topic()
