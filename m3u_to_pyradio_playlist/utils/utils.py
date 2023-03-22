"""Contain projects util functions."""


def is_not_blank(input_string: str) -> bool:
    return len(input_string.replace(" ", "")) > 0
