## Secret Santa

Janky websites.

### Example Input
INPUT: names.csv
```
# NAME,EMAIL,BLOCKLIST (Use hypen to seperate names)
Jon,jon@email.com,Jane-Adam
Adam,adam@email.com,Jon
Jane,jane@email.com,Jon
Emily,emily@email.com,
Shane,shane@email.com,Felicity
Lucy,lucy@email.com,
Craig,craig@email.com,
Megan,megan@email.com,
Felicity,felicity@email.com,Shane

```

OUTPUT:
```
Secret Santa Rolls

Giver: Jon - Reciver: Emily -- Email: jon@email.com
Giver: Adam - Reciver: Craig -- Email: adam@email.com
Giver: Jane - Reciver: Shane -- Email: jane@email.com
Giver: Emily - Reciver: Lucy -- Email: emily@email.com
Giver: Shane - Reciver: Jon -- Email: shane@email.com
Giver: Lucy - Reciver: Jane -- Email: lucy@email.com
Giver: Craig - Reciver: Adam -- Email: craig@email.com
Giver: Megan - Reciver: Felicity -- Email: megan@email.com
Giver: Felicity - Reciver: Megan -- Email: felicity@email.com
```