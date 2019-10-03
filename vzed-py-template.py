#!/bin/env python

"""

< Description of script >

Author: Vincent Zhen < Email address >

"""

from __future__ import print_function

import os
import sys
import signal
import argparse
import logging

# Optional but useful modules
"""
import subprocess as sp
from datetime import datetime # XREF: http://strftime.org/

if sys.version_info[0] < 3:
    import ConfigParser
else:
    import configparser
"""

__version__ = 0.1


# Logging configuration
LOG = logging.getLogger(__name__)

def set_stdout_output(log_level=logging.INFO):
    OUT_HANDLER = logging.StreamHandler(sys.stdout)
    OUT_HANDLER.setLevel(log_level)
    OUT_HANDLER.setFormatter(logging.Formatter('%(asctime)s - [%(levelname)s] %(message)s'))
    LOG.addHandler(OUT_HANDLER)
def set_file_output(filename, log_level=logging.INFO):
    OUT_HANDLER = logging.FileHandler(filename)
    OUT_HANDLER.setLevel(log_level)
    OUT_HANDLER.setFormatter(logging.Formatter('%(asctime)s - [%(levelname)s] %(message)s'))
    LOG.addHandler(OUT_HANDLER)

# Default signal handler
def sig_handler(signal, frame):
    LOG.warn("SIGINT/SIGTERM caught. Exiting...")
    sys.exit(1)




"""
----------------------------------------

          Your codes go here!

----------------------------------------
"""




# XREF: https://pymotw.com/3/argparse/
def set_arguments():
    parser = argparse.ArgumentParser(description="< Script description goes here >", fromfile_prefix_chars='@')

    parser.add_argument("--foo", help="Foo")

    # Argument grouping
    group_1 = parser.add_argument_group("default arguments")
    group_1.add_argument('-v', "--verbose", help="Set logging to debug", action="store_true", default=False)
    group_1.add_argument("--version", help="Get version of script", action="store_true", default=False)
    group_1.add_argument("--stdout", help="Log to stdout/terminal. Will not output to file unless requested with --output-file", action="store_true", default=False)
    group_1.add_argument("--output-file", help="Log to a specific file. Default: ./{}.log".format(os.path.splitext(__file__)[0]), metavar="OUTPUT-FILENAME", default=None, type=str, required=False)

    args = parser.parse_args()

    """
    Basic argument logic
    """
    log_level = logging.DEBUG if args.verbose else logging.INFO
    # Set base level of logging
    LOG.setLevel(log_level)
    set_stdout_output(log_level) if args.stdout else set_stdout_output(logging.ERROR)
    set_file_output(args.output_file, log_level) if args.output_file else set_file_output("{}.log".format(os.path.splitext(__file__)[0]), log_level)

    if args.version:
        print(__version__)
        sys.exit(0)

    return

def main():
    set_arguments()

    pass


if __name__ == "__main__":
    # Register signal handlers
    signal.signal(signal.SIGTERM, sig_handler)
    signal.signal(signal.SIGINT, sig_handler)

    main()
