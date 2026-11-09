from harness import row, rows_test

# fmt: off
ROWS = [
    row(["clash"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "clashes 0\n", ""),
    row(["clash"], "09:00-10:30 a\n10:00-11:00 b\n10:30-12:00 c\n11:30-12:30 d\n", 0, "a b 30 min\nb c 30 min\nc d 30 min\nclashes 3\n", ""),
    row(["clash"], "09:00-10:00 a\n10:00-11:00 b\n11:00-12:00 c\n", 0, "clashes 0\n", ""),
    row(["clash"], "08:00-18:00 offsite\n09:00-10:00 a\n09:30-09:45 b\n12:00-13:00 lunch\n", 0, "offsite a 60 min\noffsite b 15 min\noffsite lunch 60 min\na b 15 min\nclashes 4\n", ""),
    row(["clash"], "09:00-12:00 a\n09:30-11:00 b\n10:00-10:30 c\n10:15-10:20 d\n11:00-13:00 e\n", 0, "a b 90 min\na c 30 min\na d 5 min\na e 60 min\nb c 30 min\nb d 5 min\nc d 5 min\nclashes 7\n", ""),
    row(["clash"], "09:00-10:00 a\n09:00-10:00 b\n09:00-10:00 c\n", 0, "a b 60 min\na c 60 min\nb c 60 min\nclashes 3\n", ""),
    row(["clash"], "06:00-07:30 gym\n07:00-08:30 commute\n18:30-19:30 dinner\n", 0, "gym commute 30 min\nclashes 1\n", ""),
    row(["clash"], "", 0, "clashes 0\n", ""),
    row(["clash"], "09:00-09:01 blip\n", 0, "clashes 0\n", ""),
    row(["clash"], "10:00-11:00 b\n09:00-10:30 a\n", 0, "b a 30 min\nclashes 1\n", ""),
    row(["clash"], "09:00-12:00 a\n10:00-11:00 b\n10:30-11:30 c\n", 0, "a b 60 min\na c 60 min\nb c 30 min\nclashes 3\n", ""),
    row(["clash"], "09:00-10:00 z\n09:30-10:30 y\n09:45-10:15 x\n", 0, "z y 30 min\nz x 15 min\ny x 30 min\nclashes 3\n", ""),
    row(["clash"], "# off\n09:00-10:00 a\n09:59-10:30 b\n", 0, "a b 1 min\nclashes 1\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
