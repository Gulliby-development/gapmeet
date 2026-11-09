<p align="center"><img src="docs/logo.svg" width="96" alt="" /></p>

# gapmeet

[![CI](https://github.com/Gulliby-development/gapmeet/actions/workflows/ci.yml/badge.svg)](https://github.com/Gulliby-development/gapmeet/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

gapmeet is an offline command-line tool for finding free time, booked blocks, meeting collisions, and schedule statistics. It is intended for people coordinating meetings for teams, classes, and clinics. It runs on Python 3.11 or newer on Windows, macOS, and Linux and uses only the Python standard library at runtime. It needs no network access.

Run it from the repository directory with Python:

```text
python -m gapmeet COMMAND [OPTIONS]
```

The program reads meeting lines from standard input for each valid command and writes its report to standard output. It does not require installation or a separate console script. The examples below use a POSIX shell function named `gapmeet`, defined in the repository directory:

```sh
gapmeet() { python -m gapmeet "$@"; }
```

That shell function is only a convenience for POSIX-shell examples. On Windows, use `python -m gapmeet COMMAND` directly (or the equivalent Python launcher command configured on your system); no POSIX shell is required. In the final example, `2>&1` redirects standard error to standard output so the diagnostic is visible with the other output.

## Commands

```text
usage: gapmeet check [--from TIME] [--to TIME] [--min N]
       gapmeet busy [--from TIME] [--to TIME] [--min N]
       gapmeet free [--from TIME] [--to TIME] [--min N]
       gapmeet clash [--from TIME] [--to TIME] [--min N]
       gapmeet stats [--from TIME] [--to TIME] [--min N]
```

The first word selects one of five commands:

- `check` validates all meeting input and prints `ok N meeting` for one meeting, or `ok N meetings` otherwise. Skipped blank and comment lines do not count.
- `busy` merges meetings that overlap or touch into time-ordered blocks. Each line is `START-END K meeting` or `START-END K meetings`; the count is the number of meetings in that block. A final `total M min` gives the number of minutes covered by the blocks across the whole day. With no meetings it prints `total 0 min`. Window and minimum options do not affect this analysis.
- `free` finds uncovered stretches in the requested window. Each qualifying gap is printed as `START-END L min`, followed by `free F min`, the sum of the gaps shown. With no qualifying gaps it prints `free 0 min`.
- `clash` prints each pair with a positive-duration overlap as `NAME1 NAME2 M min`, ordered by the input order of the pair, followed by `clashes K`. Meetings that only touch do not clash. With no pairs it prints `clashes 0`. Window and minimum options do not affect the analysis.
- `stats` prints six lines: `meetings N`, `busy M min`, `longest L min`, `peak P`, `window W min`, and `gap G min`. These are respectively the meeting count, total occupied minutes, longest single meeting, maximum simultaneous meetings, window length, and longest free gap in that window. The longest gap is not filtered by `--min`. With no meetings, the first four values are zero, while gap equals the window length. The minimum option does not affect the analysis.

Intervals use half-open time ranges: a meeting includes its start and excludes its end. Thus touching meetings belong to the same busy block but do not overlap for `clash`. Busy totals count the union of all meeting intervals, not the sum of overlapping durations. A meeting outside a `free` or `stats` window has no effect on free time; partially intersecting meetings are clipped to the window. Options irrelevant to a command's analysis are still parsed and validated.

### Options

All commands accept these optional arguments:

- `--from TIME` sets the start of the free-time/statistics window; default `09:00`.
- `--to TIME` sets its end; default `17:00`.
- `--min N` sets the minimum free-gap length in minutes; default `1`.

A time must be exactly `HH:MM`, with ASCII digits, hours from `00` through `24`, and minutes from `00` through `59`. `24:00` is valid; no other time in hour 24 is valid. The window must start before it ends.

The minimum is a decimal integer from 1 through 240, with no leading zero. For example, `240` is valid while `0`, `007`, and `241` are not. Free gaps shorter than this value are omitted, and the free total includes only gaps shown. The window must be valid even for commands whose analysis ignores it.

Options are checked from left to right. For each recognized option, checks occur in this order: duplication, missing value, then invalid value. Thus a repeated option is reported as `given twice: OPTION` even if its second occurrence is the last word or is followed by a bad value. A non-repeated option at the end is reported as missing its value. Otherwise its next word is consumed as its value even when that word looks like another option, and that value is validated. After all words are checked, the window-order rule is applied.

## Meeting input

Provide one meeting per physical input line in this form:

```text
START-END NAME
```

A range contains exactly two valid times joined by one hyphen, such as `09:00-10:30`; its end must be later than its start. A name is 1 to 12 ASCII characters: it starts with a lowercase letter and may continue with lowercase letters, digits, or hyphens. Names must be unique.

Spaces and tabs separate the two words and may surround a line. A line containing only spaces and tabs is ignored. A line whose first word starts with `#` is a comment and is ignored; inline comments are not supported. Input is divided at line feeds. A final line without a line feed still counts, and one carriage return at the end of each line is removed. At most 40 physical lines are allowed, including blank and comment lines. Exactly 40 lines is permitted. Times and names follow the exact ASCII rules above.

## Errors and exit status

Successful commands exit with status 0, write their result only to standard output, and write nothing to standard error. Command-line errors exit with status 2; invalid meeting input exits with status 1. On either kind of failure, standard output is empty and standard error contains one line beginning `gapmeet: `.

Command-line diagnostics are:

- `gapmeet: unknown command WORD` for an unrecognized first word.
- `gapmeet: unexpected argument WORD` for an argument that is not an option, including an empty argument or `-`.
- `gapmeet: unknown option WORD` for an unrecognized option.
- `gapmeet: given twice: OPTION` when an option is repeated.
- `gapmeet: missing value for OPTION` when a non-repeated option is the last word; if the final option repeats an earlier one, `given twice: OPTION` takes precedence.
- `gapmeet: bad value for OPTION` when an option value is invalid.
- `gapmeet: window must start before it ends` when the final start is at or after the end.

For meeting input, the first invalid condition is reported using these forms:

- `gapmeet: input is too long (max 40 lines)` when there are more than 40 physical lines. This takes precedence over line-level errors.
- `gapmeet: line N: expected RANGE NAME` unless a non-comment line contains exactly two words.
- `gapmeet: line N: bad range WORD` when its range is malformed or a time is invalid.
- `gapmeet: line N: range must end after it starts` when the end is not later than the start.
- `gapmeet: line N: bad name WORD` when a name violates the format or length.
- `gapmeet: line N: duplicate name NAME` when a valid name was already used.

Line numbers count every physical line, including skipped lines. Within a line, checks occur in the order shown above: word count, range format and times, range ordering, name format, then duplicate name. Input is not read for help, version, invalid commands, or invalid options.

With no command, the five-line usage synopsis is written to standard error and the program exits with status 2. `help`, `-h`, and `--help` print that synopsis to standard output and exit 0; `--version` prints `gapmeet 0.1.0` and exits 0. These help/version forms ignore any trailing words.

## Examples

The following examples are for a POSIX shell in the repository directory, after defining the `gapmeet` function shown above:

```text
$ printf '09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n' | gapmeet free
11:30-13:00 90 min
14:00-17:00 180 min
free 270 min
$ printf '09:00-10:30 a\n10:00-11:00 b\n10:30-12:00 c\n' | gapmeet busy; printf '09:00-10:30 a\n10:00-11:00 b\n10:30-12:00 c\n' | gapmeet clash
09:00-12:00 3 meetings
total 180 min
a b 30 min
b c 30 min
clashes 2
$ printf '09:00-10:00 a\n11:00-12:00 b\n' | gapmeet stats --from 08:00 --to 13:00
meetings 2
busy 120 min
longest 60 min
peak 1
window 300 min
gap 60 min
$ printf '09:00-10:00 a\n09:30-9:45 b\n' | gapmeet check 2>&1; printf 'x' | gapmeet free --min 0 2>&1
gapmeet: line 2: bad range 09:30-9:45
gapmeet: bad value for --min
```

## Development

Use the project's virtual environment to run the automated tests and both Ruff checks:

```text
python -m pytest -q
python -m ruff check .
python -m ruff format --check .
```

Pytest and Ruff are development tools, not runtime dependencies. The runtime uses only the Python standard library.

The project is licensed under the [MIT License](LICENSE).

---

Built with [BAKED](https://github.com/Gulliby-development/baked), an open-source coding agent (bench round R95).
