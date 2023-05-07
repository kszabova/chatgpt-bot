class ResponseChecker:
    def __init__(self) -> None:
        pass

    def __call__(self, response: str) -> bool:
        raise NotImplementedError


class ToxicityChecker(ResponseChecker):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, response: str) -> bool:
        return super().__call__(response)


class TruthfulnessChecker(ResponseChecker):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, response: str) -> bool:
        return super().__call__(response)


class CompanyAttitudeChecker(ResponseChecker):
    def __init__(self) -> None:
        super().__init__()

    def __call__(self, response: str) -> bool:
        return super().__call__(response)
