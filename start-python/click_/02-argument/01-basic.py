import click

"""
poetry run python3 01-basic.py puyanh

The type of default argument is str
"""

@click.command()
@click.argument("name")
def hello(name):
    click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
