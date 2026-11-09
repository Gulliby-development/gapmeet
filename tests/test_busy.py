from harness import row, rows_test

# fmt: off
ROWS = [
    row(["busy"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "09:00-11:30 2 meetings\n13:00-14:00 1 meeting\n15:30-16:30 1 meeting\ntotal 270 min\n", ""),
    row(["busy"], "09:00-10:30 a\n10:00-11:00 b\n10:30-12:00 c\n11:30-12:30 d\n", 0, "09:00-12:30 4 meetings\ntotal 210 min\n", ""),
    row(["busy"], "09:00-10:00 a\n10:00-11:00 b\n11:00-12:00 c\n", 0, "09:00-12:00 3 meetings\ntotal 180 min\n", ""),
    row(["busy"], "08:00-18:00 offsite\n09:00-10:00 a\n09:30-09:45 b\n12:00-13:00 lunch\n", 0, "08:00-18:00 4 meetings\ntotal 600 min\n", ""),
    row(["busy"], "06:00-07:30 gym\n07:00-08:30 commute\n18:30-19:30 dinner\n", 0, "06:00-08:30 2 meetings\n18:30-19:30 1 meeting\ntotal 210 min\n", ""),
    row(["busy"], "00:00-00:30 a\n23:30-24:00 z\n", 0, "00:00-00:30 1 meeting\n23:30-24:00 1 meeting\ntotal 60 min\n", ""),
    row(["busy"], "09:00-12:00 a\n09:30-11:00 b\n10:00-10:30 c\n10:15-10:20 d\n11:00-13:00 e\n", 0, "09:00-13:00 5 meetings\ntotal 240 min\n", ""),
    row(["busy"], "09:00-10:00 a\n09:00-10:00 b\n09:00-10:00 c\n", 0, "09:00-10:00 3 meetings\ntotal 60 min\n", ""),
    row(["busy"], "09:00-09:01 blip\n", 0, "09:00-09:01 1 meeting\ntotal 1 min\n", ""),
    row(["busy"], "09:00-17:00 all\n", 0, "09:00-17:00 1 meeting\ntotal 480 min\n", ""),
    row(["busy"], "", 0, "total 0 min\n", ""),
    row(["busy"], "# none\n", 0, "total 0 min\n", ""),
    row(["busy"], "10:00-11:00 b\n09:00-10:00 a\n", 0, "09:00-11:00 2 meetings\ntotal 120 min\n", ""),
    row(["busy"], "11:00-12:00 c\n09:00-10:30 a\n10:15-11:00 b\n", 0, "09:00-12:00 3 meetings\ntotal 180 min\n", ""),
    row(["busy"], "09:00-09:30 a\r\n09:30-10:00 b\r\n", 0, "09:00-10:00 2 meetings\ntotal 60 min\n", ""),
    row(["busy", "--from", "10:00", "--to", "11:00"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "09:00-11:30 2 meetings\n13:00-14:00 1 meeting\n15:30-16:30 1 meeting\ntotal 270 min\n", ""),
    row(["busy"], "00:00-24:00 day\n", 0, "00:00-24:00 1 meeting\ntotal 1440 min\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
