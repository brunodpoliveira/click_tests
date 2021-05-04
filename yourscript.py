import click


# subgroup of commands - does not do anything useful on this toy program
@click.group()
@click.option('--verbose', is_flag=True)
def cli(verbose):
    if verbose:
        click.echo('We are in verbose mode')


@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
# write output to file, default false
@click.argument('out', type=click.File('w'), default='-', required=False)
def say(count, name, out):
    """Simple program that greets NAME for a total of COUNT times."""
    for _ in range(count):
        click.echo(f"Hello, {name}!", file=out)

# python yourscript.py --count=3
