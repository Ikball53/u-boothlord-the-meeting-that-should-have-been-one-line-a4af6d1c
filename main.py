#!/usr/bin/env python3
"""The Meeting That Should Have Been One Line.

A meeting about saving time, a follow-up to discuss saving time,
and notes in a doc nobody can find. One line says it all.
"""

MEETING_MINUTES = 47

LINE = (
    f"We spent {MEETING_MINUTES} minutes in a meeting about saving time, "
    "booked a follow-up to discuss saving time, "
    "and I took notes nobody will ever read in a doc nobody can find."
)


def main() -> None:
    print(LINE)


if __name__ == "__main__":
    main()
