"""Command-line validation and dispatch for gapmeet."""

from gapmeet.lines import parse_time
from gapmeet.registry import (
    COMMAND_TABLE,
    DEFAULT_FROM,
    DEFAULT_MIN,
    DEFAULT_TO,
    MAX_MIN,
    OPTION_NAMES,
    USAGE,
    VERSION,
    Failure,
    fail,
    reply,
)


def _validate_options(words):
    options = {"from": DEFAULT_FROM, "to": DEFAULT_TO, "min": DEFAULT_MIN}
    seen = set()
    index = 0
    while index < len(words):
        word = words[index]
        if word not in OPTION_NAMES:
            if word and word.startswith("-") and word != "-":
                fail(2, f"unknown option {word}")
            fail(2, f"unexpected argument {word}")

        if word in seen:
            fail(2, f"given twice: {word}")
        if index + 1 >= len(words):
            fail(2, f"missing value for {word}")

        value = words[index + 1]
        if word in ("--from", "--to"):
            parsed = parse_time(value)
            if parsed is None:
                fail(2, f"bad value for {word}")
            key = word[2:]
            options[key] = parsed
        else:
            if (
                not value
                or value[0] == "0"
                or len(value) > 3
                or any(char < "0" or char > "9" for char in value)
            ):
                fail(2, f"bad value for {word}")
            parsed = int(value)
            if parsed > MAX_MIN:
                fail(2, f"bad value for {word}")
            options["min"] = parsed

        seen.add(word)
        index += 2

    if options["from"] >= options["to"]:
        fail(2, "window must start before it ends")
    return options


def reads_stdin(args):
    """Return whether args select a valid command that consumes meeting input."""
    if not args or args[0] in ("help", "-h", "--help", "--version"):
        return False
    if args[0] not in (word for word, _ in COMMAND_TABLE):
        return False
    try:
        _validate_options(args[1:])
    except Failure:
        return False
    return True


def run_cli(args, text):
    """Validate a command line, dispatch it, and convert failures to replies."""
    if not args:
        return reply(2, "", USAGE)
    if args[0] in ("help", "-h", "--help"):
        return reply(0, USAGE, "")
    if args[0] == "--version":
        return reply(0, f"gapmeet {VERSION}\n", "")

    command = next((entry for entry in COMMAND_TABLE if entry[0] == args[0]), None)
    if command is None:
        return reply(2, "", f"gapmeet: unknown command {args[0]}\n")

    try:
        options = _validate_options(args[1:])
        from gapmeet import commands

        handler = getattr(commands, command[1])
        return handler(options, text)
    except Failure as failure:
        return reply(failure.status, "", f"gapmeet: {failure.message}\n")
