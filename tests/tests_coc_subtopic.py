from src.query_openai import query_openai
from src.prompt_constructor import PromptConstructor


def test_coc_subtopic_family():
    sentence = "Můžu říct svým rodičům, že Nestlé v příštím kvartálu očekává ztrátu?"
    messages = PromptConstructor.get_coc_subtopic_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_coc_subtopic_function():
    sentence = "Můžu zastávat funkci v představenstvu jiné firmy?"
    messages = PromptConstructor.get_coc_subtopic_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_coc_subtopic_noncompliance():
    sentence = "Co se stane, když poruším některou ze zásad chování?"
    messages = PromptConstructor.get_coc_subtopic_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def run_tests_coc_subtopic():
    test_coc_subtopic_family()
    test_coc_subtopic_function()
    test_coc_subtopic_noncompliance()


if __name__ == "__main__":
    run_tests_coc_subtopic()
