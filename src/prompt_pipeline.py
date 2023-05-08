from .topic_decider import TopicDecider


def prompt_pipeline(prompt: str) -> str:
    processor = TopicDecider.select_prompt_processor(prompt)
    response = processor(prompt)
    print(response)
    for checker in processor.response_checkers:
        if not checker()(response):
            print(f"Failed check in {checker}")
            return processor.default_answerer.get_default_answer(prompt, response)
    return response
