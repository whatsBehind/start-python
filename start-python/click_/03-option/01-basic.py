import click

"""
poetry run python3  01-basic.py -n Peter
"""

@click.command()
@click.option("--name", "-n", default="World", help="Input your name.")
def hello(name):
    click.echo(f"Hello {name}!")

if __name__ == '__main__':
    hello()
