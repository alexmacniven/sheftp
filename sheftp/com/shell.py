import cmd

from . import base
from .. import __version__


class Shell(base.Base):
    def run(self):
        InteractiveShell().cmdloop()


class InteractiveShell(cmd.Cmd):
    intro = '\nsheftp {0}'.format(__version__.__version__)
    prompt = '> '

    cnxn = None

    def do_ftp(self, args):
        """Creates a new FTP connection"""
        self.cnxn = ftplib.FTP(*parse(args))

    def do_exit(self, args):
        """Exits nicely"""
        try:
            self.cnxn.close()
        except:
            pass
        return True

def path_build(source, destin=None):
    """Returns full paths to source and destination"""
    if destin is None:  # no destin; use cwd
        destin = os.getcwd()
    elif destin[-1] != '/':  # destin is a full path; leave as is
        return source, destin
    # destin is a dir; join with source
    return source, os.path.join(os.path.join(destin, source))


def parse(args):
    """Converts `args` to a series of argument tuples"""
    return tuple(map(str, args.split()))
