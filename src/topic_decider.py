from prompt_processor import (
    PromptProcessor,
    BotPersonalityProcessor,
    CodeOfConductProcessor,
    DefaultPromptProcessor,
)
from utils import extract_yes_no_from_response
from query_openai import query_openai
from prompt_constructor import PromptConstructor


class TopicDecider:
    @staticmethod
    def select_prompt_processor(prompt: str) -> PromptProcessor:
        # check if the query is about Code of Conduct
        query_coc = PromptConstructor.get_is_code_of_conduct_prompt(prompt)
        response_coc = query_openai(query_coc)
        response_coc = extract_yes_no_from_response(response_coc)
        if response_coc == "ano":
            return CodeOfConductProcessor()
        # check if the query is about Bot Personality
        query_personality = PromptConstructor.get_is_bot_personality_prompt(prompt)
        response_personality = query_openai(query_personality)
        response_personality = extract_yes_no_from_response(response_personality)
        if response_personality == "ano":
            return BotPersonalityProcessor()
        # otherwise, return the default processor
        return DefaultPromptProcessor()
