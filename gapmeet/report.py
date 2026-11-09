"""Text formatting for gapmeet command reports."""


def check_report(count):
    """Return the check summary for the number of parsed meetings."""
    noun = "meeting" if count == 1 else "meetings"
    return f"ok {count} {noun}\n"


def format_time(minutes):
    """Format a minute-of-day value as a zero-padded HH:MM time."""
    hours, minute = divmod(minutes, 60)
    return f"{hours:02d}:{minute:02d}"


def busy_report(blocks):
    """Return the whole-day occupied blocks and their combined duration."""
    lines = []
    total = 0
    for start, end, count in blocks:
        noun = "meeting" if count == 1 else "meetings"
        lines.append(f"{format_time(start)}-{format_time(end)} {count} {noun}\n")
        total += end - start
    lines.append(f"total {total} min\n")
    return "".join(lines)


def free_report(gaps):
    """Return free intervals and their combined duration."""
    lines = []
    total = 0
    for start, end in gaps:
        length = end - start
        lines.append(f"{format_time(start)}-{format_time(end)} {length} min\n")
        total += length
    lines.append(f"free {total} min\n")
    return "".join(lines)


def stats_report(count, busy, longest, peak, window, gap):
    """Return the six occupancy statistics in their specified order."""
    return (
        f"meetings {count}\n"
        f"busy {busy} min\n"
        f"longest {longest} min\n"
        f"peak {peak}\n"
        f"window {window} min\n"
        f"gap {gap} min\n"
    )


def clash_report(pairs):
    """Return overlapping meeting pairs followed by their count."""
    lines = [f"{name1} {name2} {minutes} min\n" for name1, name2, minutes in pairs]
    lines.append(f"clashes {len(pairs)}\n")
    return "".join(lines)
