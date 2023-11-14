from pathlib import Path
import random
from lib import load_names_and_emails_from_csv, roll_for_matches

TEST_FILE = Path("./test_names.csv")

TEST_NAMES = {
    "Jon": ["Jane", "Adam"],
    "Adam": ["Jon"],
    "Jane": ["Jon"],
    "Emily": [""],
    "Shane": ["Felicity"],
    "Lucy": [""],
    "Craig": [""],
    "Megan": [""],
    "Felicity": ["Shane"],
}

TEST_EMAILS = {
    "Jon": "jon@email.com",
    "Adam": "adam@email.com",
    "Jane": "jane@email.com",
    "Emily": "emily@email.com",
    "Shane": "shane@email.com",
    "Lucy": "lucy@email.com",
    "Craig": "craig@email.com",
    "Megan": "megan@email.com",
    "Felicity": "felicity@email.com",
}


def test_load_names_and_emails_from_csv():
    names, emails = load_names_and_emails_from_csv(TEST_FILE)
    assert names == TEST_NAMES
    assert emails == TEST_EMAILS


TEST_MATCHES = [
    ["Jon", "Shane"],
    ["Adam", "Felicity"],
    ["Jane", "Megan"],
    ["Emily", "Craig"],
    ["Shane", "Emily"],
    ["Lucy", "Adam"],
    ["Craig", "Jon"],
    ["Megan", "Lucy"],
    ["Felicity", "Jane"],
]


def test_roll_for_matches():
    random.seed(1)

    names, _ = load_names_and_emails_from_csv(TEST_FILE)
    matches = roll_for_matches(names)

    assert matches == TEST_MATCHES


if __name__ == "__main__":
    test_load_names_and_emails_from_csv()
    test_roll_for_matches()
