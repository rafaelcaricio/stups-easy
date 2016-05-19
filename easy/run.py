#!/usr/bin/env python3
import sys
from subprocess import PIPE, Popen
from typing import Optional


class CliWrapper:
    def __init__(self, application: str) -> None:
        self.application = application

    def _execute(self, args: list) -> None:
        command = [self.application]
        command.extend(args)
        print('Translated to STUPS command: {}'.format(' '.join(command)))
        process = Popen(command, stdout=PIPE, stderr=sys.stderr)
        stdout, stderr = process.communicate()
        if stdout:
            print(stdout.decode())


def artifacts_cmd(subcommands: list) -> None:
    """translated to pierone"""
    pierone = CliWrapper('pierone')
    subcommands = subcommands[1:]

    if len(subcommands) > 0 and 'list' == subcommands[0]:
        subcommands[0] = 'artifacts'

    pierone._execute(subcommands)


def deploy_cmd(subcommands: list) -> None:
    """translated to senza"""
    senza = CliWrapper('senza')
    senza._execute(subcommands[1:])


def mai_cmd(subcommands: list) -> None:
    """translated to mai"""
    mai = CliWrapper('mai')
    mai._execute(subcommands[1:])


def piu_cmd(subcommands: list) -> None:
    """translated to piu"""
    piu = CliWrapper('piu')
    piu._execute(subcommands[1:])


def fullstop_cmd(subcommands: list) -> None:
    """translated to fullstop"""
    fullstop = CliWrapper('fullstop')
    fullstop._execute(subcommands[1:])


def kio_cmd(subcommands: list) -> None:
    """translated to kio"""
    kio = CliWrapper('kio')
    kio._execute(subcommands)


def kio_applications_cmd(subcommands: list) -> None:
    """translated to kio applications"""
    kio = CliWrapper('kio')
    subcommands[0] = 'applications'
    kio._execute(subcommands)


COMMAND_WRAPPERS = {
    'artifacts': artifacts_cmd,
    'deploy': deploy_cmd,
    'login': mai_cmd,
    'ssh': piu_cmd,
    'compliance': fullstop_cmd,
    'versions': kio_cmd,
    'applications': kio_applications_cmd
}


def help_cmd(*subcommands: Optional[list]) -> None:
    """show help and exit"""
    print('Available options:')
    col_width = max(len(x) for x in COMMAND_WRAPPERS)
    for subcommand in sorted(COMMAND_WRAPPERS):
        cmd_func = COMMAND_WRAPPERS[subcommand]
        print('\t{:{}}\t{}'.format(subcommand, col_width,
                                   cmd_func.__doc__))
    sys.exit(1)


def main() -> None:
    COMMAND_WRAPPERS['help'] = help_cmd

    args = sys.argv[1:]
    if len(args) == 0:
        print('Missing arguments.\n')
        help_cmd()

    subcommand = COMMAND_WRAPPERS.get(args[0], help_cmd)
    subcommand(args)

if __name__ == '__main__':
    main()
