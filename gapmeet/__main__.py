"""python -m gapmeet: the only module that reads or writes a stream."""

import sys

from gapmeet.cli import reads_stdin, run_cli


def main():
    args = sys.argv[1:]
    text = sys.stdin.buffer.read().decode("utf-8", errors="replace") if reads_stdin(args) else ""
    answer = run_cli(args, text)
    sys.stdout.buffer.write(answer["out"].encode("utf-8"))
    sys.stderr.buffer.write(answer["err"].encode("utf-8"))
    sys.stdout.flush()
    sys.stderr.flush()
    return answer["status"]


if __name__ == "__main__":
    sys.exit(main())
