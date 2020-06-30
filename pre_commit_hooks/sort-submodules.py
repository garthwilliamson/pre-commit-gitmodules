#!/usr/bin/env python3

from configparser import ConfigParser

import sh
import sys


def find_indent(filename):
    """ Find the indent type of this file.

    This function assumes consistant indentation.

    Args:
        filename: The filename to look in.
    Returns:
        N spaces if indented with 2 or 4 spaces, or a tab char if indented
        with tabs.

    """
    with open(filename) as f:
        for l in f:
            if "\t" in l:
                return "\t"
            if "    " in l:
                return "    "
            if "  " in l:
                return "  "


for filename in sh.git("--no-pager", "diff", "--cached", "--name-only").split("\n"):
    if filename == ".gitmodules":
        indent = find_indent(".gitmodules")
        config = ConfigParser()
        config.read(".gitmodules")

        with open(".gitmodules", "w") as gitmodules:
            for section in sorted(config.sections()):
                gitmodules.write("[{}]\n".format(section))
                for k, v in config[section].items():
                    if k != "branch":
                        gitmodules.write("{}{} = {}\n".format(indent, k, v))
        sh.git("add", ".gitmodules")
