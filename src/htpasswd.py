#!/usr/bin/env python
"""Replacement for htpasswd"""
# Original author: Eli Carter
# Obtained from https://gist.github.com/eculver/1420227

import os
import sys
import random
from optparse import OptionParser

# We need a crypt module, but Windows doesn't have one by default.  Try to find
# one, and tell the user if we can't.
try:
    import crypt
except ImportError:
    try:
        import fcrypt as crypt
    except ImportError:
        sys.stderr.write("Cannot find a crypt module.  "
                         "Possibly http://carey.geek.nz/code/python-fcrypt/\n")
        sys.exit(1)


def salt():
    """Returns a string of 2 random letters"""
    letters = 'abcdefghijklmnopqrstuvwxyz' \
              'ABCDEFGHIJKLMNOPQRSTUVWXYZ' \
              '0123456789/.'
    return random.choice(letters) + random.choice(letters)


class HtpasswdFile:
    """A class for manipulating htpasswd files."""

    def __init__(self, filename):
        self.entries = []
        self.filename = filename

    def save(self):
        """Write the htpasswd file to disk"""
        open(self.filename, 'w').writelines(["%s:%s\n" % (entry[0], entry[1])
                                             for entry in self.entries])

    def update(self, username, password):
        """Replace the entry for the given user, or add it if new."""
        pwhash = crypt.crypt(password, salt())
        self.entries.append([username, pwhash])


def main():
    """%prog filename
    Create an htpasswd file"""
    # For now, we only care about the use cases that affect tests/functional.py
    parser = OptionParser(usage=main.__doc__)

    options, args = parser.parse_args()

    def syntax_error(msg):
        """Utility function for displaying fatal error messages with usage
        help.
        """
        sys.stderr.write("Syntax error: " + msg)
        sys.stderr.write(parser.get_usage())
        sys.exit(1)

    # Non-option arguments
    if len(args) < 1:
        syntax_error("Insufficient number of arguments.\n")
    filename = args[0]

    passwdfile = HtpasswdFile(filename)

    username = os.environ['PASSTHRU_USERNAME']
    password = os.environ['PASSTHRU_PASSWORD']

    passwdfile.update(username, password)

    passwdfile.save()


if __name__ == '__main__':
    main()
