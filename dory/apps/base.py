import json
import sys
from subprocess import PIPE, Popen
from typing import Iterable


class CliWrapper:
    def __init__(self, application: str):
        self.application = application

    def _execute(self, *args: Iterable[str]):
        command = [self.application]
        command.extend(args)
        process = Popen(command, stdout=PIPE, stderr=sys.stderr)
        stdout, stderr = process.communicate()
        if stdout:
            print(stdout.decode())
