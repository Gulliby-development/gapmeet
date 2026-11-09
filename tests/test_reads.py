from harness import reads_rows, row

# fmt: off
ROWS = [
    row(["check"], "", 1, "", ""),
    row(["busy"], "", 1, "", ""),
    row(["free"], "", 1, "", ""),
    row(["clash"], "", 1, "", ""),
    row(["stats"], "", 1, "", ""),
    row(["free", "--min", "30"], "", 1, "", ""),
    row(["free", "--from", "08:00", "--to", "18:00", "--min", "240"], "", 1, "", ""),
    row(["help"], "", 0, "", ""),
    row(["-h"], "", 0, "", ""),
    row(["--help"], "", 0, "", ""),
    row(["--version"], "", 0, "", ""),
    row([], "", 0, "", ""),
    row(["frob"], "", 0, "", ""),
    row([""], "", 0, "", ""),
    row(["check", "x"], "", 0, "", ""),
    row(["free", "--min"], "", 0, "", ""),
    row(["free", "--min", "0"], "", 0, "", ""),
    row(["free", "--min", "241"], "", 0, "", ""),
    row(["free", "--from", "10:00", "--from", "11:00"], "", 0, "", ""),
    row(["free", "--from", "17:00"], "", 0, "", ""),
    row(["free", "--to", "24:00"], "", 1, "", ""),
    row(["free", "--to", "24:01"], "", 0, "", ""),
    row(["free", "--bogus"], "", 0, "", ""),
    row(["Free"], "", 0, "", ""),
    row(["--min", "5"], "", 0, "", ""),
    row(["stats", "--from", "09:00", "--to", "09:00"], "", 0, "", ""),
]
# fmt: on

test_rows = reads_rows(ROWS)
