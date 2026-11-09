from harness import row, rows_test

# fmt: off
ROWS = [
    row(["check", "x"], "", 2, "", "gapmeet: unexpected argument x\n"),
    row(["check", ""], "", 2, "", "gapmeet: unexpected argument \n"),
    row(["busy", "-"], "", 2, "", "gapmeet: unexpected argument -\n"),
    row(["check", "--nope"], "", 2, "", "gapmeet: unknown option --nope\n"),
    row(["free", "--from"], "", 2, "", "gapmeet: missing value for --from\n"),
    row(["free", "--from", "9:00"], "", 2, "", "gapmeet: bad value for --from\n"),
    row(["free", "--from", "09:60"], "", 2, "", "gapmeet: bad value for --from\n"),
    row(["free", "--to", "24:01"], "", 2, "", "gapmeet: bad value for --to\n"),
    row(["free", "--from", ""], "", 2, "", "gapmeet: bad value for --from\n"),
    row(["free", "--min"], "", 2, "", "gapmeet: missing value for --min\n"),
    row(["free", "--min", "0"], "", 2, "", "gapmeet: bad value for --min\n"),
    row(["free", "--min", "007"], "", 2, "", "gapmeet: bad value for --min\n"),
    row(["free", "--min", "241"], "", 2, "", "gapmeet: bad value for --min\n"),
    row(["free", "--min", "240"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "free 0 min\n", ""),
    row(["free", "--from", "10:00", "--from", "11:00"], "", 2, "", "gapmeet: given twice: --from\n"),
    row(["stats", "--min", "5", "--min", "6"], "", 2, "", "gapmeet: given twice: --min\n"),
    row(["free", "--from", "--to"], "", 2, "", "gapmeet: bad value for --from\n"),
    row(["free", "--to", "--min", "5"], "", 2, "", "gapmeet: bad value for --to\n"),
    row(["free", "--min", "5", "x"], "", 2, "", "gapmeet: unexpected argument x\n"),
    row(["free", "--from", "10:00", "--to", "10:00"], "", 2, "", "gapmeet: window must start before it ends\n"),
    row(["free", "--from", "17:00"], "", 2, "", "gapmeet: window must start before it ends\n"),
    row(["free", "--to", "09:00"], "", 2, "", "gapmeet: window must start before it ends\n"),
    row(["free", "--to", "24:00", "--from", "23:59"], "", 0, "23:59-24:00 1 min\nfree 1 min\n", ""),
    row(["free", "--from", "08:00", "--to", "18:00", "--min", "30"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "08:00-09:00 60 min\n11:30-13:00 90 min\n14:00-15:30 90 min\n16:30-18:00 90 min\nfree 330 min\n", ""),
    row(["free", "--min", "0", "--bogus"], "", 2, "", "gapmeet: bad value for --min\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
