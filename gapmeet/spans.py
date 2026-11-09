"""Interval arithmetic for busy time, free gaps, and concurrency."""


def busy_blocks(meetings):
    """Return maximal busy intervals with the number of meetings in each block."""
    ordered = sorted(meetings, key=lambda meeting: (meeting[0], meeting[1]))
    blocks = []
    for start, end, _name in ordered:
        if blocks and start <= blocks[-1][1]:
            block_start, block_end, count = blocks[-1]
            blocks[-1] = (block_start, max(block_end, end), count + 1)
        else:
            blocks.append((start, end, 1))
    return blocks


def free_gaps(meetings, start, end):
    """Return every positive uncovered interval clipped to the given window."""
    cursor = start
    gaps = []
    ordered = sorted(meetings, key=lambda meeting: (meeting[0], meeting[1]))
    for meeting_start, meeting_end, _name in ordered:
        if meeting_end <= start or meeting_start >= end:
            continue
        clipped_start = max(meeting_start, start)
        clipped_end = min(meeting_end, end)
        if clipped_start > cursor:
            gaps.append((cursor, clipped_start))
        cursor = max(cursor, clipped_end)
    if cursor < end:
        gaps.append((cursor, end))
    return gaps


def peak(meetings):
    """Return the greatest number of concurrent half-open meeting intervals."""
    events = []
    for start, end, _name in meetings:
        events.append((start, 1))
        events.append((end, -1))

    concurrent = 0
    maximum = 0
    for _time, delta in sorted(events, key=lambda event: (event[0], event[1])):
        concurrent += delta
        maximum = max(maximum, concurrent)
    return maximum


def clashes(meetings):
    """Return overlapping meeting pairs in their original input order."""
    pairs = []
    for first_index, (first_start, first_end, first_name) in enumerate(meetings):
        for second_start, second_end, second_name in meetings[first_index + 1 :]:
            minutes = min(first_end, second_end) - max(first_start, second_start)
            if minutes > 0:
                pairs.append((first_name, second_name, minutes))
    return pairs
