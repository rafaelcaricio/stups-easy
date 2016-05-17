#!/usr/bin/env python3
import click
from clickclick import AliasedGroup
from dory.version import print_version
from dory.apps.base import CliWrapper

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.group(cls=AliasedGroup, context_settings=CONTEXT_SETTINGS)
@click.option('-v', '--version', is_flag=True, callback=print_version,
              expose_value=False, is_eager=True,
              help='Print the current version number and exit.')
def cli():
    pass


@cli.command()
@click.argument('subcommands', nargs=-1)
def artifacts(subcommands):
    if subcommands:
        pierone = CliWrapper('pierone')
        subcommands = list(subcommands)

        if 'list' == subcommands[0]:
            subcommands[0] = 'artifacts'

        pierone._execute(*subcommands)


@cli.command()
@click.argument('subcommands', nargs=-1)
def deploy(subcommands):
    if subcommands:
        senza = CliWrapper('senza')
        senza._execute(*subcommands)
