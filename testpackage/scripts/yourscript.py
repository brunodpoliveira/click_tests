import click


class Config(object):
    def __init__(self):
        self.verbose = False


# the config class data will be passed using
# pass_config. ensure=True will make sure the decorator class
# is created on first usage
pass_config = click.make_pass_decorator(Config, ensure=True)


# subgroup of commands - does not do anything useful on this toy program
@click.group()
@click.option('--verbose', is_flag=True)
@click.option('--home-directory', type=click.Path())
# write output to file, default false
@click.argument('out', type=click.File('w'), default='-', required=False)
@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory


@cli.command()
#TODO --count and --name does not work - do research why and fix it
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
# write output to file, default false
@click.argument('out', type=click.File('w'), default='-', required=False)
@pass_config
def greet(config, count, name, out):
    """Simple program that greets NAME for a total of COUNT times."""
    if config.verbose:
        click.echo('We are in verbose mode')
    click.echo('Home Directory is %s' % config.home_directory)

    for _ in range(count):
        click.echo(f"Hello, {name}!", file=out)

# python yourscript.py --count=3
