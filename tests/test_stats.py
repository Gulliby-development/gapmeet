from harness import row, rows_test

# fmt: off
ROWS = [
    row(["stats"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "meetings 4\nbusy 270 min\nlongest 90 min\npeak 1\nwindow 480 min\ngap 90 min\n", ""),
    row(["stats"], "", 0, "meetings 0\nbusy 0 min\nlongest 0 min\npeak 0\nwindow 480 min\ngap 480 min\n", ""),
    row(["stats"], "09:00-10:30 a\n10:00-11:00 b\n10:30-12:00 c\n11:30-12:30 d\n", 0, "meetings 4\nbusy 210 min\nlongest 90 min\npeak 2\nwindow 480 min\ngap 270 min\n", ""),
    row(["stats"], "09:00-10:00 a\n10:00-11:00 b\n11:00-12:00 c\n", 0, "meetings 3\nbusy 180 min\nlongest 60 min\npeak 1\nwindow 480 min\ngap 300 min\n", ""),
    row(["stats"], "08:00-18:00 offsite\n09:00-10:00 a\n09:30-09:45 b\n12:00-13:00 lunch\n", 0, "meetings 4\nbusy 600 min\nlongest 600 min\npeak 3\nwindow 480 min\ngap 0 min\n", ""),
    row(["stats"], "00:00-00:30 a\n23:30-24:00 z\n", 0, "meetings 2\nbusy 60 min\nlongest 30 min\npeak 1\nwindow 480 min\ngap 480 min\n", ""),
    row(["stats"], "09:00-12:00 a\n09:30-11:00 b\n10:00-10:30 c\n10:15-10:20 d\n11:00-13:00 e\n", 0, "meetings 5\nbusy 240 min\nlongest 180 min\npeak 4\nwindow 480 min\ngap 240 min\n", ""),
    row(["stats"], "09:00-10:00 a\n09:00-10:00 b\n09:00-10:00 c\n", 0, "meetings 3\nbusy 60 min\nlongest 60 min\npeak 3\nwindow 480 min\ngap 420 min\n", ""),
    row(["stats"], "09:00-17:00 all\n", 0, "meetings 1\nbusy 480 min\nlongest 480 min\npeak 1\nwindow 480 min\ngap 0 min\n", ""),
    row(["stats"], "09:20-09:30 a\n10:00-10:10 b\n11:00-12:00 c\n16:50-17:00 d\n", 0, "meetings 4\nbusy 90 min\nlongest 60 min\npeak 1\nwindow 480 min\ngap 290 min\n", ""),
    row(["stats", "--from", "08:00", "--to", "18:00"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "meetings 4\nbusy 270 min\nlongest 90 min\npeak 1\nwindow 600 min\ngap 90 min\n", ""),
    row(["stats", "--from", "10:00", "--to", "10:30"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "meetings 4\nbusy 270 min\nlongest 90 min\npeak 1\nwindow 30 min\ngap 0 min\n", ""),
    row(["stats", "--from", "00:00", "--to", "24:00"], "09:00-10:00 standup\n10:00-11:30 design\n13:00-14:00 lunch\n15:30-16:30 review\n", 0, "meetings 4\nbusy 270 min\nlongest 90 min\npeak 1\nwindow 1440 min\ngap 540 min\n", ""),
]
# fmt: on

test_rows = rows_test(ROWS)
