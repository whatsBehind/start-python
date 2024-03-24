import click

"""
poetry run python3 02-chaining-command.py init deploy

Click support chaining multiple commands together so that they can be run in sequence with a single invocation
To enable this, you set `chain=True` in the `@click.group()` decorator
"""

@click.group(chain=True)
def cli():
    pass

@cli.command("init")
def init():
    click.echo("Init...")

@cli.command("deploy")
def deploy():
    click.echo("Deploying...")

if __name__ == '__main__':
    cli()

