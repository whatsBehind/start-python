import click

"""
poetry run python3 04-value-types.py --level debug

You can specify the type of value an option should accept using the type parameter. 
This ensures that the user input is validated and converted to the correct type. 
Common types include str, int, float, bool, and click.Choice for a set of fixed values
"""

@click.command()
@click.option("--level", type=click.Choice(["info", "debug", "warning", "error"], case_sensitive=False), help="Logging level")
def log(level):
    click.echo(f"Logging at {level.upper()} level")

if __name__ == '__main__':
    log()
