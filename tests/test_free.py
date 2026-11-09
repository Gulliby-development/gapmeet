from harness import row, rows_test

# fmt: off
ROWS = [
    row(["free"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "11:30-13:00 90 min\n14:00-15:30 90 min\n16:30-17:00 30 min\nfree 210 min\n", ""),
    row(["free"], "", 0, "09:00-17:00 480 min\nfree 480 min\n", ""),
    row(["free"], "09:00-10:00 a\n10:00-11:00 b\n11:00-12:00 c\n", 0, "12:00-17:00 300 min\nfree 300 min\n", ""),
    row(["free"], "08:00-18:00 offsite\n09:00-10:00 a\n09:30-09:45 b\n12:00-13:00 lunch\n", 0, "free 0 min\n", ""),
    row(["free"], "00:00-00:30 a\n23:30-24:00 z\n", 0, "09:00-17:00 480 min\nfree 480 min\n", ""),
    row(["free"], "09:20-09:30 a\n10:00-10:10 b\n11:00-12:00 c\n16:50-17:00 d\n", 0, "09:00-09:20 20 min\n09:30-10:00 30 min\n10:10-11:00 50 min\n12:00-16:50 290 min\nfree 390 min\n", ""),
    row(["free"], "09:00-17:00 all\n", 0, "free 0 min\n", ""),
    row(["free", "--min", "30"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "11:30-13:00 90 min\n14:00-15:30 90 min\n16:30-17:00 30 min\nfree 210 min\n", ""),
    row(["free", "--min", "61"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "11:30-13:00 90 min\n14:00-15:30 90 min\nfree 180 min\n", ""),
    row(["free", "--min", "11"], "09:20-09:30 a\n10:00-10:10 b\n11:00-12:00 c\n16:50-17:00 d\n", 0, "09:00-09:20 20 min\n09:30-10:00 30 min\n10:10-11:00 50 min\n12:00-16:50 290 min\nfree 390 min\n", ""),
    row(["free", "--min", "10"], "09:20-09:30 a\n10:00-10:10 b\n11:00-12:00 c\n16:50-17:00 d\n", 0, "09:00-09:20 20 min\n09:30-10:00 30 min\n10:10-11:00 50 min\n12:00-16:50 290 min\nfree 390 min\n", ""),
    row(["free", "--from", "08:00", "--to", "18:00"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "08:00-09:00 60 min\n11:30-13:00 90 min\n14:00-15:30 90 min\n16:30-18:00 90 min\nfree 330 min\n", ""),
    row(["free", "--from", "10:30", "--to", "14:30"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "11:30-13:00 90 min\n14:00-14:30 30 min\nfree 120 min\n", ""),
    row(["free", "--from", "00:00", "--to", "24:00"], "00:00-00:30 a\n23:30-24:00 z\n", 0, "00:30-23:30 1380 min\nfree 1380 min\n", ""),
    row(["free", "--from", "09:30", "--to", "09:45"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "free 0 min\n", ""),
    row(["free", "--from", "09:00", "--to", "09:01"], "09:00-09:01 blip\n", 0, "free 0 min\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
