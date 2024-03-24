import click

"""
poetry run python 05-eager-option.py --version

```
CLI Application Version 1.0
```

Eager options allow you to perform the callback function immediately
w/o waiting for the rest of the command line arguments to be processed
Often, eager options don't need to pass a value to the command function,
so setting `expose_value=False` prevents the option's value from being passed
as an argument to the command function.

When running this script, text "Running command..." is not printed because 
the process exits in the callback function which is run immediately
"""
def print_version(ctx, param, value):
    click.echo("CLI Application Version 1.0")
    ctx.exit()

@click.command()
@click.option(
    '--version', 
    is_flag=True, 
    is_eager=True, 
    callback=print_version,
    expose_value=False, 
    help="Show the version and exit."
)
def cli():
    click.echo('Running command...')

if __name__ == '__main__':
    cli()
