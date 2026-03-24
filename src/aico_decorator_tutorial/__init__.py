import click
from .basic_functions import main as basic_main
from .error_handling import main as error_main


@click.group("decorators")
def main():
    pass


for command in [basic_main, error_main]:
    main.add_command(command)
