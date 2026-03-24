"""
In Python, decorators can be applied in two ways:

1. Using the decorator @ symbol:

@my_decorator
def my_func(*args, **kwargs):
    print("function called")


2. Using the decorator function:

def my_func(*args, **kwargs):
    print("function called")

decorated_func = my_decorator(my_func)
"""

import click
import json
from typing import Any
from .utils.decorators import my_decorator


# Functions to be decorated
def read_message(dict: dict) -> tuple:
    if len(dict) > 1:
        raise ValueError("Dictionary must contain only one key-value pair")
    return list(dict.items())[0]


def transform_message(key: str, value: dict) -> tuple:
    if not isinstance(value, str):
        raise ValueError("Value must be a string")
    new_value = value.upper() + "_transformed"
    return key, new_value


def write_message(key: str, value: Any) -> dict:
    return {key: value}


def process(message: dict) -> dict:
    key, value = read_message(message)
    new_key, new_value = transform_message(key, value)
    return write_message(new_key, new_value)


# Decorated functions
read_message = my_decorator(read_message)
transform_message = my_decorator(transform_message)
write_message = my_decorator(write_message)
process = my_decorator(process)


# Main
@click.command("logging")
def main() -> None:
    input_message = json.load(open("src/fixtures/basic.json"))
    print(f"input_message={input_message}")

    output_message = process(input_message)

    print("Process complete")
    print(f"output_message={output_message}")


if __name__ == "__main__":
    main()
