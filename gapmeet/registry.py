"""Shared constants and helpers of gapmeet: the version, the limits, the usage text, the command table, fail() and reply()."""

VERSION = "0.1.0"
MAX_LINES = 40
MAX_NAME = 12
MAX_MIN = 240
DAY = 1440
DEFAULT_FROM = 540
DEFAULT_TO = 1020
DEFAULT_MIN = 1

USAGE = (
    "usage: gapmeet check [--from TIME] [--to TIME] [--min N]\n"
    "       gapmeet busy [--from TIME] [--to TIME] [--min N]\n"
    "       gapmeet free [--from TIME] [--to TIME] [--min N]\n"
    "       gapmeet clash [--from TIME] [--to TIME] [--min N]\n"
    "       gapmeet stats [--from TIME] [--to TIME] [--min N]\n"
)

# One entry per command: its word and the name of the function of gapmeet/commands.py that runs it.
COMMAND_TABLE = (
    ("check", "check_command"),
    ("busy", "busy_command"),
    ("free", "free_command"),
    ("clash", "clash_command"),
    ("stats", "stats_command"),
)

OPTION_NAMES = ("--from", "--to", "--min")


class Failure(Exception):
    """A failure that ends the command: status 1 for the input, 2 for the command line."""

    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


def fail(status, message):
    raise Failure(status, message)


def reply(status, out, err):
    return {"status": status, "out": out, "err": err}
