from .prompts.prompts import *
from .prompts.code_of_conduct_subtopics import *


class PromptConstructor:
    @staticmethod
    def get_is_code_of_conduct_prompt(sentence: str) -> list:
        messages = [
            {"role": "system", "content": SYSTEM_ONE_WORD},
            {"role": "user", "content": TOPIC_CODE_OF_CONDUCT},
            {"role": "user", "content": SENTENCE_ANSWER.format(sentence=sentence)},
        ]
        return messages

    @staticmethod
    def get_is_bot_personality_prompt(sentence: str) -> list:
        messages = [
            {"role": "system", "content": SYSTEM_ONE_WORD},
            {"role": "user", "content": TOPIC_BOT_PERSONALITY},
            {"role": "user", "content": SENTENCE_ANSWER.format(sentence=sentence)},
        ]
        return messages

    @staticmethod
    def get_coc_subtopic_prompt(sentence: str) -> list:
        messages = [
            {"role": "system", "content": SYSTEM_NUMBER},
            {"role": "user", "content": SUBTOPIC_CODE_OF_CONDUCT},
            {"role": "user", "content": SENTENCE_ANSWER.format(sentence=sentence)},
        ]
        return messages

    @staticmethod
    def get_coc_answer_prompt(sentence: str, subtopic: int) -> list:
        messages = [
            {"role": "system", "content": SYSTEM_INSTRUCT},
            {"role": "system", "content": SYSTEM_LANGUAGE},
            {
                "role": "user",
                "content": ANSWER_CODE_OF_CONDUCT.format(text=COC_SUBTOPICS[subtopic]),
            },
            {"role": "user", "content": SENTENCE_ANSWER.format(sentence=sentence)},
        ]
        return messages

    @staticmethod
    def get_bot_personality_answer_prompt(sentence: str) -> list:
        messages = [
            {"role": "system", "content": SYSTEM_INSTRUCT},
            {"role": "system", "content": SYSTEM_HUMAN},
            {"role": "user", "content": SENTENCE_ANSWER.format(sentence=sentence)},
        ]
        return messages

    @staticmethod
    def get_default_answer_prompt(sentence: str) -> list:
        messages = [
            {"role": "system", "content": SYSTEM_INSTRUCT},
            {"role": "user", "content": ANSWER_DEFAULT},
            {"role": "user", "content": SENTENCE_ANSWER.format(sentence=sentence)},
        ]
        return messages

    @staticmethod
    def get_check_toxicity_prompt(sentence: str) -> list:
        messages = [
            {"role": "system", "content": SYSTEM_ONE_WORD},
            {"role": "user", "content": CHECK_TOXICITY},
            {"role": "user", "content": SENTENCE_ANSWER.format(sentence=sentence)},
        ]
        return messages

    @staticmethod
    def get_check_truthfulness_prompt(sentence: str) -> list:
        messages = [
            {"role": "system", "content": SYSTEM_ONE_WORD},
            {"role": "user", "content": CHECK_TRUTHFULNESS},
            {"role": "user", "content": SENTENCE_ANSWER.format(sentence=sentence)},
        ]
        return messages

    @staticmethod
    def get_check_attitude_prompt(sentence: str) -> list:
        messages = [
            {"role": "system", "content": SYSTEM_ONE_WORD},
            {"role": "user", "content": CHECK_ATTITUDE},
            {"role": "user", "content": SENTENCE_ANSWER.format(sentence=sentence)},
        ]
        return messages
