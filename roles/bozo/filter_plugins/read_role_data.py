#!/usr/bin/env python
from __future__ import print_function
import os
import re

FN_RELEASE_NOTES = ('RELEASE_NOTES.md', 'release_notes.md')
RE_RELEASE_NOTES_HEADLINE = re.compile(
    r'^#+\s+([\d.]+)\s+-\s+(\d{4}-\d{2}-\d{2})$')


class FilterModule(object):
    """Required for filter providers."""

    def filters(self):
        """Advertises provided plugins.

        Maps plugin names to the implementing function.
        """
        return {
            'read_role_version': read_role_version,
        }


def find_release_notes(role_path):
    if role_path:
        for filename in FN_RELEASE_NOTES:
            if filename in os.listdir(role_path):
                return os.path.join(role_path, filename)
    return None


def read_role_version(role_path):
    rn_file = find_release_notes(role_path)
    if rn_file:
        with open(rn_file, 'r') as fh:
            match = re.match(RE_RELEASE_NOTES_HEADLINE, fh.next())
            if match:
                return match.group(1)
    return None


if __name__ == '__main__':
    print('''

    This script is to be used as an Ansible filter.

    ''')
