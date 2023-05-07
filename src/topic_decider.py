from prompt_processor import PromptProcessor


class TopicDecider:
    def __init__(self) -> None:
        raise NotImplemented

    def select_prompt_processor(self, prompt: str) -> PromptProcessor:
        raise NotImplemented
