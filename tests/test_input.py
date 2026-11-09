from harness import row, rows_test

# fmt: off
ROWS = [
    row(["check"], "", 0, "ok 0 meetings\n", ""),
    row(["check"], "09:00-10:00 a\n", 0, "ok 1 meeting\n", ""),
    row(["check"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "ok 4 meetings\n", ""),
    row(["check"], "# note\n\n  \n09:00-10:00 a\n\t\n#09:00-10:00 b\n", 0, "ok 1 meeting\n", ""),
    row(["check"], "09:00-10:00 a\r\n10:00-11:00 b\r\n", 0, "ok 2 meetings\n", ""),
    row(["check"], "09:00-10:00 a", 0, "ok 1 meeting\n", ""),
    row(["check"], "\t09:00-10:00\t a \t\n", 0, "ok 1 meeting\n", ""),
    row(["check"], "09:00-10:00 a # not a comment\n", 1, "", "gapmeet: line 1: expected RANGE NAME\n"),
    row(["check"], "9:00-10:00 a\n", 1, "", "gapmeet: line 1: bad range 9:00-10:00\n"),
    row(["check"], "09:00-10:00\n", 1, "", "gapmeet: line 1: expected RANGE NAME\n"),
    row(["check"], "09:00-1000 a\n", 1, "", "gapmeet: line 1: bad range 09:00-1000\n"),
    row(["check"], "09:60-10:00 a\n", 1, "", "gapmeet: line 1: bad range 09:60-10:00\n"),
    row(["check"], "24:01-24:30 a\n", 1, "", "gapmeet: line 1: bad range 24:01-24:30\n"),
    row(["check"], "10:00-10:00 a\n", 1, "", "gapmeet: line 1: range must end after it starts\n"),
    row(["check"], "10:00-09:00 a\n", 1, "", "gapmeet: line 1: range must end after it starts\n"),
    row(["check"], "24:00-24:00 a\n", 1, "", "gapmeet: line 1: range must end after it starts\n"),
    row(["check"], "09:00-10:00 A\n", 1, "", "gapmeet: line 1: bad name A\n"),
    row(["check"], "09:00-10:00 1a\n", 1, "", "gapmeet: line 1: bad name 1a\n"),
    row(["check"], "09:00-10:00 a-b-2\n", 0, "ok 1 meeting\n", ""),
    row(["check"], "09:00-10:00 a\n10:00-11:00 a\n", 1, "", "gapmeet: line 2: duplicate name a\n"),
    row(["check"], "09:00-10:00 a b\n", 1, "", "gapmeet: line 1: expected RANGE NAME\n"),
    row(["check"], "09:00-10:00 a\n09:00-10:00\n", 1, "", "gapmeet: line 2: expected RANGE NAME\n"),
    row(["check"], "09:00-10:00 a\n\n\n10:00-11:00 b\n", 0, "ok 2 meetings\n", ""),
    row(["check"], "09:00-10:00 a\r10:00-11:00 b\n", 1, "", "gapmeet: line 1: expected RANGE NAME\n"),
    row(["check"], "09:00-10:00 a\n1x:00-10:00 b\n09:00-10:00 a\n", 1, "", "gapmeet: line 2: bad range 1x:00-10:00\n"),
    row(["check"], "09:00-10:00 a\n10:00-11:00 a\nbad\n", 1, "", "gapmeet: line 2: duplicate name a\n"),
]
# fmt: on

test_rows = rows_test(ROWS)
