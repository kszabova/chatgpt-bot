from .response_checker import (
    TruthfulnessChecker,
    CompanyAttitudeChecker,
)
from .default_answerer import DefaultAnswerer
from .prompt_constructor import PromptConstructor
from .query_openai import query_openai

from .utils import extract_number_from_response


class PromptProcessor:
    def __init__(self) -> None:
        self.response_checkers = []
        self.default_answerer = DefaultAnswerer()

    def __call__(self, prompt: str) -> str:
        return self.get_response(prompt)

    def preprocess_prompt(self, prompt: str) -> str:
        raise NotImplementedError

    def get_system_response(self, prompt: str) -> str:
        raise NotImplementedError

    def postprocess_response(self, response: str) -> str:
        raise NotImplementedError

    def get_response(self, prompt: str) -> str:
        prompt = self.preprocess_prompt(prompt)
        response = self.get_system_response(prompt)
        response = self.postprocess_response(response)
        return response


class BotPersonalityProcessor(PromptProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.response_checkers = [CompanyAttitudeChecker]

    def __call__(self, prompt: str) -> str:
        return super().__call__(prompt)

    def preprocess_prompt(self, prompt: str) -> str:
        return prompt

    def get_system_response(self, prompt: str) -> str:
        messages = PromptConstructor.get_bot_personality_answer_prompt(prompt)
        response = query_openai(messages)
        return response

    def postprocess_response(self, response: str) -> str:
        return response


class CodeOfConductProcessor(PromptProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.response_checkers = [CompanyAttitudeChecker]

    def __call__(self, prompt: str) -> str:
        return super().__call__(prompt)

    def preprocess_prompt(self, prompt: str) -> str:
        return prompt

    def get_system_response(self, prompt: str) -> str:
        messages_subtopic = PromptConstructor.get_coc_subtopic_prompt(prompt)
        response_subtopic = query_openai(messages_subtopic)
        subtopic = extract_number_from_response(response_subtopic)
        # if we couldn't find subtopic number, return empty response
        if subtopic is None:
            return ""
        messages = PromptConstructor.get_coc_answer_prompt(prompt, subtopic)
        response = query_openai(messages)
        return response

    def postprocess_response(self, response: str) -> str:
        return response


class DefaultPromptProcessor(PromptProcessor):
    def __init__(self) -> None:
        super().__init__()
        self.response_checkers = [
            TruthfulnessChecker,
            CompanyAttitudeChecker,
        ]

    def __call__(self, prompt: str) -> str:
        return super().__call__(prompt)

    def preprocess_prompt(self, prompt: str) -> str:
        return prompt

    def get_system_response(self, prompt: str) -> str:
        messages = PromptConstructor.get_default_answer_prompt(prompt)
        response = query_openai(messages)
        return response

    def postprocess_response(self, response: str) -> str:
        return response
