import click

"""
poetry run python3 03-nesting-command.py database insert

You can also nest command groups, creating a hierarchical structure of commands. 
This is useful for organizing subcommands under a common group.
"""

@click.group()
def cli():
    pass

@cli.group()
def database():
    pass

@database.command("insert")
def insert():
    click.echo("Inserting a new entry...")

@database.command("deploy")
def delete():
    click.echo("Deleting an entry...")

if __name__ == '__main__':
    cli()
