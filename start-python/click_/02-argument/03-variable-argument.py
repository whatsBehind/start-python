import click

"""
poetry run python3 03-variable-argument.py src tst
"""

@click.command()
@click.argument('files', nargs=-1)
def touch(files):
    click.echo(f"Touching files {files}")

if __name__ == '__main__':
    touch()
