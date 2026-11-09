"""The helper of the row files: a row is row(args, input, status, out, err) or, for reads_rows, row(args, "", reads, "", "")."""

import pytest

from gapmeet.cli import reads_stdin, run_cli


def row(args, text, status, out, err):
    return (args, text, status, out, err)


def rows_ids(rows):
    return ["row%d" % number for number in range(1, len(rows) + 1)]


def rows_test(rows):
    @pytest.mark.parametrize(("args", "text", "status", "out", "err"), rows, ids=rows_ids(rows))
    def test_rows(args, text, status, out, err):
        answer = run_cli(args, text)
        assert (answer["status"], answer["out"], answer["err"]) == (status, out, err)

    return test_rows


def reads_rows(rows):
    @pytest.mark.parametrize(("args", "text", "reads", "out", "err"), rows, ids=rows_ids(rows))
    def test_reads(args, text, reads, out, err):
        assert reads_stdin(args) == (reads == 1)

    return test_reads
