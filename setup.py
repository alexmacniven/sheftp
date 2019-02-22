import codecs
import os
import sys

from setuptools import find_packages, setup


# Package meta-data
NAME = 'sheftp'
DESCRIPTION = 'Flavours of FTP in an interactive shell'
URL = 'https://github.com/alexmacniven/sheftp'
EMAIL = 'macniven.ap@gmail.com'
AUTHOR = 'Alex Macniven'

# What packages are required for this module to be executed?
REQUIRED = [
    'docopt'
]

# Install packages not on PyPi.
# DEPENDENCIES = [
# ]

# Import the README and use it as the long-description
# Note: README.md needs to be in the MANIFEST
here = os.path.abspath(os.path.dirname(__file__))
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary
about = {}
with open(os.path.join(here, NAME, '__version__.py')) as f:
    exec(f.read(), about)

# Where the magic happens:
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    # If your package is a single module, use this instead of 'packages':
    # py_modules=['mypackage'],
    # If the package is not intended to be used from the console, you
    # can comment out 'entry_points'
    entry_points={
        'console_scripts': ["{0}={0}.cli:main".format(NAME)],
    },
    install_requires=REQUIRED,
    include_package_data=True,
    # dependency_links=DEPENDENCIES,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: ISC License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ]
)
