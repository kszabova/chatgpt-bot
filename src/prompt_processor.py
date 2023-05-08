class PromptProcessor:
    def __init__(self) -> None:
        pass

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

    def __call__(self, prompt: str) -> str:
        return super().__call__(prompt)

    def preprocess_prompt(self, prompt: str) -> str:
        return super().preprocess_prompt(prompt)

    def get_system_response(self, prompt: str) -> str:
        return super().get_system_response(prompt)

    def postprocess_response(self, response: str) -> str:
        return super().postprocess_response(response)

    def get_response(self, prompt: str) -> str:
        return super().get_response(prompt)


class CodeOfConductProcessor(PromptProcessor):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, prompt: str) -> str:
        return super().__call__(prompt)

    def preprocess_prompt(self, prompt: str) -> str:
        return super().preprocess_prompt(prompt)

    def get_system_response(self, prompt: str) -> str:
        return super().get_system_response(prompt)

    def postprocess_response(self, response: str) -> str:
        return super().postprocess_response(response)

    def get_response(self, prompt: str) -> str:
        return super().get_response(prompt)


class DefaultPromptProcessor(PromptProcessor):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, prompt: str) -> str:
        return super().__call__(prompt)

    def preprocess_prompt(self, prompt: str) -> str:
        return super().preprocess_prompt(prompt)

    def get_system_response(self, prompt: str) -> str:
        return super().get_system_response(prompt)

    def postprocess_response(self, response: str) -> str:
        return super().postprocess_response(response)

    def get_response(self, prompt: str) -> str:
        return super().get_response(prompt)
