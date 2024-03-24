import click

"""
poetry run python3 04-callback-input.py --age 1

```
Error: Invalid value for '--age': You must be at least 18 years old.
```

You can create custom validation functions and use them with `callback` parameter of 
options and arguments to process the input entered by user
"""

def validate_age(ctx, param, value):
    if value < 18:
        raise click.BadParameter("You must be at least 18 years old.")
    return value

@click.command()
@click.option("--age", type=int, callback=validate_age)
def signup(age):
    click.echo(f"Welcome! Your age is {age}")

if __name__ == '__main__':
    signup()
