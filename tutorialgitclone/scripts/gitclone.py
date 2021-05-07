import os
import click


class Repo(object):
    def __init__(self, home=None, debug=False):
        self.home = os.path.abspath(home or '.')
        self.debug = False


pass_repo = click.make_pass_decorator(Repo, ensure=True)


@click.group()
@click.option('--repo-home', envvar='REPO_HOME', default='.repo')
@click.option('--debug/--no-debug', default=False, envvar='REPO_DEBUG')
@click.pass_context
def cli(ctx, repo_home, debug):
    ctx.obj = Repo(repo_home, debug)


@cli.command()
@click.argument('src')
@click.argument('dest', required=False)
@pass_repo
def clone(repo, src, dest):
    click.echo(isinstance(repo, Repo))
