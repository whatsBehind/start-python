import click

"""
poetry run python3 02-customize-help-messages.py --help

you can use the epilog parameter of the @click.command() or @click.group() decorators 
to add text that will be displayed at the end of the help message
"""

@click.command(epilog="Type 'poetry run python3 02-customize-help-messages.py --help' for more information")
@click.option("--name", "-n", default="World", help="The name to greet.")
def greet(name):
    click.echo(f"Hello {name}!")

if __name__ == '__main__':
    greet()
