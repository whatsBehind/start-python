import click

"""
poetry run python3 03-context-settings.py --h

In this case, we've changed the default help options to -h and --help, 
demonstrating how you can adjust context settings to suit your preferences
"""
@click.group(context_settings={'help_option_names': ['-h', '--help']})
def cli():
    pass

@cli.command()
def init():
    click.echo("Initiating...")

if __name__ == '__main__':
    cli()
