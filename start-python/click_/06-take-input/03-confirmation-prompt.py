import click

"""
poetry run python3 03-confirmation-prompt.py

Prompts for confirmation (yes/no question)
Set argument abort to True, when you confirm with `n`, the cli quits
"""

@click.command()
def delete():
    click.confirm("Are you sure you want to delete this?", abort=True)
    click.echo("Deleted!")

if __name__ == '__main__':
    delete()
