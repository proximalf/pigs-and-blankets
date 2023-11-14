from pathlib import Path

from lib import load_names_and_emails_from_csv, roll_for_matches, write_matches
from mail import send_emails
import random

DEBUG = True
PATH = "./test_names.csv"


def main(debug: bool = True) -> None:
    """
    Entry point.

    Secret Santa script, refer to test_names for input.
    """
    path = Path(PATH)
    names, emails = load_names_and_emails_from_csv(path)

    matches = roll_for_matches(names)

    write_matches(path, matches, emails)

    if not debug:
        send_emails(matches, emails)


if __name__ == "__main__":
    main(DEBUG)
