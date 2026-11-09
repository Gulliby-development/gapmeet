from harness import row, rows_test

# fmt: off
ROWS = [
    row([], "", 2, "", "usage: gapmeet check [--from TIME] [--to TIME] [--min N]\n       gapmeet busy [--from TIME] [--to TIME] [--min N]\n       gapmeet free [--from TIME] [--to TIME] [--min N]\n       gapmeet clash [--from TIME] [--to TIME] [--min N]\n       gapmeet stats [--from TIME] [--to TIME] [--min N]\n"),
    row(["help"], "", 0, "usage: gapmeet check [--from TIME] [--to TIME] [--min N]\n       gapmeet busy [--from TIME] [--to TIME] [--min N]\n       gapmeet free [--from TIME] [--to TIME] [--min N]\n       gapmeet clash [--from TIME] [--to TIME] [--min N]\n       gapmeet stats [--from TIME] [--to TIME] [--min N]\n", ""),
    row(["-h", "extra"], "", 0, "usage: gapmeet check [--from TIME] [--to TIME] [--min N]\n       gapmeet busy [--from TIME] [--to TIME] [--min N]\n       gapmeet free [--from TIME] [--to TIME] [--min N]\n       gapmeet clash [--from TIME] [--to TIME] [--min N]\n       gapmeet stats [--from TIME] [--to TIME] [--min N]\n", ""),
    row(["--help", "--bogus"], "", 0, "usage: gapmeet check [--from TIME] [--to TIME] [--min N]\n       gapmeet busy [--from TIME] [--to TIME] [--min N]\n       gapmeet free [--from TIME] [--to TIME] [--min N]\n       gapmeet clash [--from TIME] [--to TIME] [--min N]\n       gapmeet stats [--from TIME] [--to TIME] [--min N]\n", ""),
    row(["--version"], "", 0, "gapmeet 0.1.0\n", ""),
    row(["--version", "x"], "", 0, "gapmeet 0.1.0\n", ""),
    row(["frob"], "", 2, "", "gapmeet: unknown command frob\n"),
    row([""], "", 2, "", "gapmeet: unknown command \n"),
    row(["Check"], "", 2, "", "gapmeet: unknown command Check\n"),
    row(["--from"], "", 2, "", "gapmeet: unknown command --from\n"),
    row(["--min", "5"], "", 2, "", "gapmeet: unknown command --min\n"),
    row(["help", "free"], "", 0, "usage: gapmeet check [--from TIME] [--to TIME] [--min N]\n       gapmeet busy [--from TIME] [--to TIME] [--min N]\n       gapmeet free [--from TIME] [--to TIME] [--min N]\n       gapmeet clash [--from TIME] [--to TIME] [--min N]\n       gapmeet stats [--from TIME] [--to TIME] [--min N]\n", ""),
    row(["free"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "11:30-13:00 90 min\n14:00-15:30 90 min\n16:30-17:00 30 min\nfree 210 min\n", ""),
    row(["check"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "ok 4 meetings\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
