from typing import Optional


def extract_yes_no_from_response(response: str) -> Optional[str]:
    response = response.lower()
    if response[:3] == "yes":
        return "yes"
    elif response[:2] == "no":
        return "no"
    return None


def extract_number_from_response(response: str) -> Optional[int]:
    number_str = ""
    for c in response:
        if c in "0123456789":
            number_str += c
        else:
            break
    return int(number_str) if number_str else None
