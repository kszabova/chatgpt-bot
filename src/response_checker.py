from .query_openai import query_openai
from .prompt_constructor import PromptConstructor

from .utils import extract_yes_no_from_response


class ResponseChecker:
    def __init__(self) -> None:
        pass

    def __call__(self, response: str) -> bool:
        """
        Returns True if response can be shown to user,
        False otherwise.
        """
        raise NotImplementedError


class TruthfulnessChecker(ResponseChecker):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, response: str) -> bool:
        messages = PromptConstructor.get_check_truthfulness_prompt(response)
        response = query_openai(messages)
        response = extract_yes_no_from_response(response)
        # only return True if the system is sure it's true
        if response is not None and response == "ano":
            return True
        return False


class CompanyAttitudeChecker(ResponseChecker):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, response: str) -> bool:
        messages = PromptConstructor.get_check_attitude_prompt(response)
        response = query_openai(messages)
        response = extract_yes_no_from_response(response)
        # only return True if the system is positive that
        # the response can't harm the reputation of the company
        if response is not None and response == "ne":
            return True
        return False
