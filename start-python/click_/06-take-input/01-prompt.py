import click

"""
poetry run python3 01-prompt.py

```
Please enter your username: Peter
Please enter your password:
Hello, Peter, you are logged in!
```

click.prompt() is used to ask the user for a username and a password, 
with the password input being hidden.
"""

@click.command()
def login():
    username = click.prompt("Please enter your username")
    password = click.prompt("Please enter your password", hide_input=True)
    click.echo(f"Hello, {username}, you are logged in!")

if __name__ == '__main__':
    login()