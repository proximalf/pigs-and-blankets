from pathlib import Path
from typing import Dict, List, Tuple
import numpy as np
import random


def load_names_and_emails_from_csv(path: Path) -> Tuple[Dict[str, str], Dict[str, str]]:
    """
    Load secret santa list.
    Expects a file with 3 columns in format, NAME,EMAIL,BLOCKLIST (Use hypen to seperate names)
    """

    names, addresses, blockers = np.loadtxt(
        path, unpack=True, dtype=str, delimiter=",", skiprows=1
    )

    names = list(names)

    addresses = list(addresses)

    emails = {name: address for name, address in zip(names, addresses)}

    blockers = [row.split("-") for row in list(blockers)]
    names_and_blockers = {name: block_list for name, block_list in zip(names, blockers)}
    return names_and_blockers, emails


def roll_for_matches(
    names: Dict[str, List[str]], roll_limit=1000
) -> List[Tuple[str, str]]:
    """
    Return list of names in format, giver, receiver.
    """
    draw = list(names.keys()).copy()
    matches = []

    for giver in names.keys():
        receiver = None
        rolls = 0

        # Cycle through draw pile until a successful draw
        while True:
            receiver = random.choice(draw)
            rolls += 1
            if (
                receiver not in names[giver]
                and giver != receiver
                or rolls >= roll_limit
            ):
                break

        matches.append([giver, receiver])
        # Remove a successful draw
        draw.remove(receiver)

    if rolls > 100:
        # If Roll limit reached reroll
        matches = roll_for_matches(names, roll_limit)

    return matches


def write_matches(
    path: Path, matches: List[Tuple[str, str]], emails: Dict[str, str]
) -> None:
    output_str = "Secret Santa Rolls\n"

    for giver, receiver in matches:
        output_str += (
            f"\nGiver: {giver} - Reciver: {receiver} -- Email: {emails[giver]}"
        )

    output = path.parent / "output"

    output.write_text(output_str)
