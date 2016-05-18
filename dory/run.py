#!/usr/bin/env python3
import sys
from subprocess import PIPE, Popen


class CliWrapper:
    def __init__(self, application: str):
        self.application = application

    def _execute(self, args: list):
        command = [self.application]
        command.extend(args)
        print('Translated to STUPS command: {}'.format(' '.join(command)))
        process = Popen(command, stdout=PIPE, stderr=sys.stderr)
        stdout, stderr = process.communicate()
        if stdout:
            print(stdout.decode())


def artifacts_cmd(subcommands):
    pierone = CliWrapper('pierone')
    subcommands = subcommands[1:]

    if len(subcommands) > 1 and 'list' == subcommands[0]:
        subcommands[0] = 'artifacts'

    pierone._execute(subcommands)


def deploy_cmd(subcommands):
    senza = CliWrapper('senza')
    senza._execute(subcommands[1:])


def mai_cmd(subcommands):
    mai = CliWrapper('mai')
    mai._execute(subcommands[1:])


def piu_cmd(subcommands):
    piu = CliWrapper('piu')
    piu._execute(subcommands[1:])


def fullstop_cmd(subcommands):
    fullstop = CliWrapper('fullstop')
    fullstop._execute(subcommands[1:])


def kio_cmd(subcommands):
    kio = CliWrapper('kio')
    kio._execute(subcommands)


def kio_applications_cmd(subcommands):
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
    'application-versions': kio_applications_cmd
}

COMMAND_DESCRIPTIONS = {
    'artifacts': 'translated to pierone',
    'deploy': 'translated to senza',
    'login': 'translated to mai',
    'ssh': 'translated to piu',
    'compliance': 'translated to fullstop',
    'versions': 'translated to kio',
    'application-versions': 'translated to kio',
    'help': 'just print this and exit'
}


def help_cmd(*subcommands):
    print('Available options:')
    col_width = max(len(x) for x in COMMAND_WRAPPERS)
    for subcommand in sorted(COMMAND_WRAPPERS):
        print('\t{:{}}\t{}'.format(subcommand, col_width,
                                   COMMAND_DESCRIPTIONS[subcommand]))
    sys.exit(1)


def main():
    COMMAND_WRAPPERS['help'] = help_cmd

    args = sys.argv[1:]
    if len(args) == 0:
        print('Missing arguments.\n')
        help_cmd()

    subcommand = COMMAND_WRAPPERS.get(args[0], help_cmd)
    subcommand(args)

if __name__ == '__main__':
    main()
