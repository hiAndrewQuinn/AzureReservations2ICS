import csv
import os
import json

import ics
import click
import arrow


# The utf-8-sig is because the CSV file downloaded from Azure
# has a BOM (Byte Order Mark) at the beginning of the file.
@click.command()
@click.argument("csvfile", type=click.File("r", encoding="utf-8-sig"))
def csv2ics(csvfile):
    # Get the name sans extension of the CSV file.
    # This will be used as the name of the ICS file.
    icsfile = csvfile.name.split(".")[0] + ".ics"

    # If the ICS file already exists, delete it.
    try:
        os.remove(icsfile)
    except OSError:
        pass

    reader = csv.DictReader(csvfile)
    cal = ics.Calendar()

    for row in reader:
        # Pretty print the row.
        event = ics.Event()

        event.name = f'Azure reservation expiring: {row["Name"]}'
        event.begin = row["Expiration date"]
        event.end = row["Expiration date"]
        event.description = "An Azure reservation ends today."

        cal.events.add(event)

        with open(icsfile, "w") as f:
            f.writelines(cal)


def main():
    csv2ics()


if __name__ == "__main__":
    main()
