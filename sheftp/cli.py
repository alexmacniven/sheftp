"""
sheftp

Usage:
  sheftp shell
  sheftp -h | --help
  sheftp --version

Options:
  -h --help                     Show this screen.
  --version                     Show version.

Examples:
  shell                         Opens an interactive shell  


Help:
  For help using this tool, please open an issue on the repository:

"""

import inspect
from docopt import docopt
from .__version__ import __version__


def main():
    """Entry point for any console commands"""
    # Import the commands and let docopt parse the options and args
    # from the CLI.
    import sheftp.com as com
    options = docopt(__doc__, version=__version__)
    # Each option has passed has the name of the option as 'key' and
    # whether it was passed (true/false) as 'val'.
    # Eg: {'routes': true}
    for (key, val) in options.items():
        # If the commands package has a module named 'key' and its
        # 'val' is true (it's been passed)...
        if hasattr(com, key) and val:
            # Look for the corresponding class in the module and invoke
            # its constructor.
            module = getattr(com, key)
            com = inspect.getmembers(module, inspect.isclass)
            command = [c[1] for c in com if c[0] == key.capitalize()][0]
            command = command(options)
            # Invoke the command objects run function to do the 'work'.
            command.run()
