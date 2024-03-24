import click

"""
poetry run python3 03-multiple-values.py -n Peter James

Flags are a special kind of boolean options that do not take any arguments. 
They are True if specified on the command line and False otherwise. 
Flags can be defined by setting is_flag=True in the click.option() decorator
"""

@click.command()
@click.option("--names", "-n", nargs=2, help="First and last name")
def hello(names):
    # click.echo(f"Hello {" ".join(names)}!")
    click.echo(f'Hello {" ".join(names)}!')

if __name__ == '__main__':
    hello()
