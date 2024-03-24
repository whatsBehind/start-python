import click

"""
poetry run python3  02-flags.py -n Peter --upper-case

Flags are a special kind of boolean options that do not take any arguments. 
They are True if specified on the command line and False otherwise. 
Flags can be defined by setting is_flag=True in the click.option() decorator
"""

@click.command()
@click.option("--name", "-n", default="World", help="Input your name.")
@click.option("--upper-case", "-u", is_flag=True, help="Print your name in upper case")
def hello(name, upper_case):
    your_name = name.upper() if upper_case else name
    click.echo(f"Hello {your_name}!")

if __name__ == '__main__':
    hello()
