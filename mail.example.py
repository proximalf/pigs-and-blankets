from typing import Dict, List, Tuple
import yagmail

USERNAME = "USERNAME"
TOKEN = "TOKEN"


def send_emails(matches: List[Tuple[str, str]], emails: Dict[str, str]) -> None:
    """
    Send emails using yagmail.

    Matches = [("Jon", "Craig"), ...]
    Emails = {"Jon": "jon@email.com", ...}
    """
    yag = yagmail.SMTP(USERNAME, TOKEN)

    subject = "Secret Santa"
    for giver, receiver in matches:
        msg = f"<b>Congrats {giver}! You have drawn, {receiver}!<b>"
        yag.send(emails[giver], subject, msg)
