import click

"""
poetry run python3 04-argument-types.py 1 2

"""

@click.command()
@click.argument('n1', type=int)
@click.argument('n2', type=int)
def plus(n1, n2):
    result = n1 + n2
    click.echo(f"{n1} + {n2} is equal to {result}")

if __name__ == '__main__':
    plus()
