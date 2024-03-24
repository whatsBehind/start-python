import click

"""
poetry run python3 01-auto-help-generation.py --help

```
Usage: 01-auto-help-generation.py [OPTIONS]

Options:
  -n, --name TEXT  The name to greet.
  --help           Show this message and exit.
```

Click automatically generates help pages for all commands and groups. This is done using
the `-help` option, which is available by default for every command.
"""

@click.command()
@click.option("--name", "-n", default="World", help="The name to greet.")
def greet(name):
    click.echo(f"Hello {name}!")

if __name__ == '__main__':
    greet()
