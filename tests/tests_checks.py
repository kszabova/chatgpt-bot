from src.query_openai import query_openai
from src.prompt_constructor import PromptConstructor


def test_check_toxicity_yes():
    sentence = "Myslím, že jste příliš hloupý, abyste u nás pracoval."
    messages = PromptConstructor.get_check_toxicity_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_check_toxicity_no():
    sentence = "Děkujeme za zájem o práci v naší společnosti. Ozveme se vám do týdne."
    messages = PromptConstructor.get_check_toxicity_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_check_truthfulness_yes():
    sentence = (
        "Firma Nestlé se zabývá výrobou potravin a nápojů, jako jsou například káva, "
        "čokoláda, cereálie, mléčné výrobky, dětská výživa a mnoho dalšího."
    )
    messages = PromptConstructor.get_check_truthfulness_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_check_truthfulness_no():
    sentence = (
        "Firma Nestlé se zabývá výrobou potravin a nápojů, jako jsou například káva, "
        "auta, nábytek a mnoho dalšího."
    )
    messages = PromptConstructor.get_check_truthfulness_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_check_attitude_yes():
    sentence = (
        "Firma Nestlé se zabývá výrobou potravin a nápojů, jako je například káva, "
        "a bývá obviňováná z přílišného využívání vody v oblastech domorodých Američanů."
    )
    messages = PromptConstructor.get_check_attitude_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def test_check_attitude_no():
    sentence = (
        "Firma Nestlé se zabývá výrobou potravin a nápojů, jako jsou například káva, "
        "čokoláda, cereálie, mléčné výrobky, dětská výživa a mnoho dalšího."
    )
    messages = PromptConstructor.get_check_attitude_prompt(sentence)
    response = query_openai(messages)
    print("PROMPT:\n", messages)
    print("RESPONSE:\n", response)


def run_tests_checks():
    test_check_toxicity_yes()
    test_check_toxicity_no()
    test_check_truthfulness_yes()
    test_check_truthfulness_no()
    test_check_attitude_yes()
    test_check_attitude_no()


if __name__ == "__main__":
    run_tests_checks()
