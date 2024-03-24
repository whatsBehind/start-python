import click

"""
poetry run python3 02-prompt-option.py

You can also specify that an option should prompt the user is not provided on the command line
If you run this script w/o the `--name` option, Click will prompt you for the name
"""

@click.command()
@click.option("--name", prompt=True)
def login(name):
    click.echo(f"Hello, {name}, you are logged in!")

if __name__ == '__main__':
    login()
