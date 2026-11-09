"""Time and meeting-input parsing for gapmeet."""

from gapmeet.registry import MAX_LINES, MAX_NAME, fail


def parse_time(word):
    """Return minutes after midnight for an exact ASCII HH:MM time, or None."""
    if (
        len(word) != 5
        or word[2] != ":"
        or not ("0" <= word[0] <= "9")
        or not ("0" <= word[1] <= "9")
        or not ("0" <= word[3] <= "9")
        or not ("0" <= word[4] <= "9")
    ):
        return None

    hour = int(word[:2])
    minute = int(word[3:])
    if minute > 59 or hour > 24 or (hour == 24 and minute != 0):
        return None
    return hour * 60 + minute


def _valid_name(name):
    if not name or len(name) > MAX_NAME or not ("a" <= name[0] <= "z"):
        return False
    return all("a" <= char <= "z" or "0" <= char <= "9" or char == "-" for char in name[1:])


def read_meetings(text):
    """Parse meetings in input order, failing on the first invalid line."""
    if not text:
        lines = []
    else:
        lines = text.split("\n")
        if lines[-1] == "":
            lines.pop()

    if len(lines) > MAX_LINES:
        fail(1, "input is too long (max 40 lines)")

    meetings = []
    names = set()
    for number, line in enumerate(lines, start=1):
        if line.endswith("\r"):
            line = line[:-1]
        stripped = line.strip(" \t")
        if not stripped:
            continue
        words = _split_words(stripped)
        if words[0].startswith("#"):
            continue
        if len(words) != 2:
            fail(1, f"line {number}: expected RANGE NAME")

        range_word, name = words
        if range_word.count("-") != 1:
            fail(1, f"line {number}: bad range {range_word}")
        start_word, end_word = range_word.split("-")
        start = parse_time(start_word)
        end = parse_time(end_word)
        if start is None or end is None:
            fail(1, f"line {number}: bad range {range_word}")
        if end <= start:
            fail(1, f"line {number}: range must end after it starts")
        if not _valid_name(name):
            fail(1, f"line {number}: bad name {name}")
        if name in names:
            fail(1, f"line {number}: duplicate name {name}")
        names.add(name)
        meetings.append((start, end, name))
    return meetings


def _split_words(line):
    """Split a trimmed line on runs of ASCII spaces or tabs only."""
    words = []
    current = []
    for char in line:
        if char in " \t":
            if current:
                words.append("".join(current))
                current = []
        else:
            current.append(char)
    if current:
        words.append("".join(current))
    return words
