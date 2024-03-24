import click

"""
poetry run python3 02-multiple-arguments.py src tst

Define two arguments
"""

@click.command()
@click.argument("source")
@click.argument("destination")
def copy(source, destination):
    """Copy a file from SOURCE to DESTINATION"""
    click.echo(f"Copying a file from {source} to {destination}")

if __name__ == '__main__':
    copy()
