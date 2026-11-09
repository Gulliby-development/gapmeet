"""Command handlers for gapmeet."""

from gapmeet.lines import read_meetings
from gapmeet.registry import reply
from gapmeet.report import busy_report, check_report, clash_report, free_report, stats_report
from gapmeet.spans import busy_blocks, clashes, free_gaps, peak


def check_command(options, text):
    """Validate meeting input and report its meeting count."""
    meetings = read_meetings(text)
    return reply(0, check_report(len(meetings)), "")


def busy_command(options, text):
    """Report the whole-day busy blocks, ignoring window options."""
    meetings = read_meetings(text)
    return reply(0, busy_report(busy_blocks(meetings)), "")


def free_command(options, text):
    """Report qualifying free gaps within the requested window."""
    meetings = read_meetings(text)
    gaps = free_gaps(meetings, options["from"], options["to"])
    visible_gaps = [gap for gap in gaps if gap[1] - gap[0] >= options["min"]]
    return reply(0, free_report(visible_gaps), "")


def clash_command(options, text):
    """Report every overlapping meeting pair, ignoring window options."""
    meetings = read_meetings(text)
    return reply(0, clash_report(clashes(meetings)), "")


def stats_command(options, text):
    """Report meeting, occupancy, concurrency, and window statistics."""
    meetings = read_meetings(text)
    blocks = busy_blocks(meetings)
    busy = sum(end - start for start, end, _count in blocks)
    longest = max((end - start for start, end, _name in meetings), default=0)
    window = options["to"] - options["from"]
    gaps = free_gaps(meetings, options["from"], options["to"])
    longest_gap = max((end - start for start, end in gaps), default=0)
    report = stats_report(len(meetings), busy, longest, peak(meetings), window, longest_gap)
    return reply(0, report, "")
