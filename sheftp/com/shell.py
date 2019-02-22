import cmd

from . import base
from .. import __version__


class Shell(base.Base):
    def run(self):
        InteractiveShell().cmdloop()


class InteractiveShell(cmd.Cmd):
    intro = '\nsheftp {0}'.format(__version__.__version__)
    prompt = '>> '

    def do_exit(self, inp):
        """Exits nicely"""
        return True
