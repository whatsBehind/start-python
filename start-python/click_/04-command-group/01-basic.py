import click

"""
poetry run python3 01-basic.py init

Command groups are a way to bundle several commands into a single program. 
This is especially useful for complex CLI applications that need to provide 
users with a variety of related operations. 
Groups are created with the @click.group() decorator

In below example, `cli` is a command group that contains two commands: `init` and `deploy`
"""

@click.group()
def cli():
    pass

@cli.command()
def init():
    click.echo("Init...")

@cli.command()
def deploy():
    click.echo("Deploying...")

if __name__ == '__main__':
    cli()

