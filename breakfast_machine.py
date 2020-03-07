#!/usr/bin/env python3

"""
    breakfast_machine.py

    Automates the creation of Way of Steel magic items with random properties
"""


import argparse
import logging
import signal
import sys


def parse_args(args):
    """Returns list of arguments excluding program name
    """

    parser = argparse.ArgumentParser(
                description="Automates the creation of random WoS magic items")

    parser.add_argument("-v",
                        "--verbose",
                        help="Output more process information to console",
                        action="store_true")

    return parser.parse_args(args)


def config_logging(verbose):
    """Configures logging for breakfast_machine
    """

    handlers = list()

    fh = logging.FileHandler(filename="breakfast_machine.log")
    handlers.append(fh)

    if verbose:
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.INFO)
        handlers.append(ch)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%d-%m-%y %H:%M",
        handlers=handlers)

    return logging.getLogger("breakfast_machine")


def sig_handler(signal, frame):
    """Cleanly handle a keyboard interrupt
    """

    sys.exit(0)


def main():
    """Main function of breakfast_machine
    """

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    args = parse_args(sys.argv[1:])

    logger = config_logging(args.verbose)
    logger.info("breakfast_machine invoked:")

if __name__ == "__main__":
    main()
