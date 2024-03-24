import click

"""
poetry run python3 05-required-options.py -username Peter

Sometimes you want to make an option mandatory. You can do this by setting `required=True`
"""

@click.command()
@click.option("--username", required=True, help="Your username")
def login(username):
    click.echo(f"User {username} is logging in...")

if __name__ == '__main__':
    login()
