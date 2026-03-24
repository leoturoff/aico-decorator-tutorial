import click
import json
from .utils.decorators import debug_with_exits
from .utils.exceptions import TookTooLong, BelowThreshold, SillyName


# Decorated functions
@debug_with_exits
def read_message(dict: dict) -> tuple:
    if len(dict) > 1:
        raise ValueError("Dictionary must contain only one key-value pair")
    return list(dict.items())[0]


@debug_with_exits
def check_name(key: str, value: float) -> tuple:
    if key == "ryan":
        raise SillyName("Nobody is really named Ryan, right?")
    return key, value


@debug_with_exits
def check_value(key: str, value: float) -> tuple:
    if value < 0.5:
        raise BelowThreshold("Value is below threshold.")
    return key, value


@debug_with_exits
def wait_for(*args, seconds: int) -> tuple:
    if seconds > 5:
        raise TookTooLong("This is taking too long, I can't wait 5 seconds.")
    return args


@debug_with_exits
def write_message(key: str, value: float) -> dict:
    return {key: value}


@debug_with_exits
def process(message: dict) -> dict:
    key, value = read_message(message)
    key, value = check_name(key, value)
    key, value = check_value(key, value)
    key, value = wait_for(key, value, seconds=2)
    return write_message(key, value)


# Main
@click.command("exceptions")
def main() -> None:
    input_message = json.load(open("src/fixtures/error.json"))
    print(f"input_message={input_message}")

    output_message = process(input_message)

    print("Process complete")
    print(f"output_message={output_message}")


if __name__ == "__main__":
    main()
