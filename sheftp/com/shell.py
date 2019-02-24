import cmd
import ftplib
import os

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

    def do_list(self, args):
        """Lists directory contents"""
        # TODO: Check valid args
        # headnames = '\t\t\t'.join(['Name', 'Type', 'Size', 'Mod'])
        # print(headnames)
        list_dir(self.cnxn)

    def do_pull(self, args):
        """Downloads a file"""
        # TODO: Will this download a directory?
        source, destin = path_build(*parse(args))
        with open(destin, 'wb') as destin_file:
            self.cnxn.retrbinary(
                'RETR {0}'.format(source), destin_file.write, 1024
            )

    def do_exit(self, args):
        """Exits nicely"""
        try:
            self.cnxn.close()
        except:
            pass
        return True


def list_dir(cnxn, path='.'):
    """Lists contents of an FTP directory"""
    for name, stats in cnxn.mlsd(path):
        itype = stats['type']
        if itype == 'dir':
            list_dir(cnxn, '{0}/{1}'.format(path, name))
        else:
            print('{0}'.format('{0}/{1}'.format(path, name)))


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
