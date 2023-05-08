class DefaultAnswerer:
    def __init__(self) -> None:
        self.answer = (
            "Bohužel, s vaším dotazem vám nemohu pomoct. "
            "Prosím, obraťte se na personální oddělení "
            "na telefonním čísle 123 456 789."
        )

    def get_default_answer(self, prompt, response):
        return self.answer
