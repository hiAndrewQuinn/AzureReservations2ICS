Azure Reservation CSV to `.ics` / ICal file
==================================

An issue came up with a customer recently where we keep forgetting
to book our Azure reservations, so I decided to write this little
CSV to ICS wrapper.

## Quickstart

```bash
pip install ics
pip install click

git clone https://github.com/hiAndrewQuinn/AzureReservations2ICS.git
cd AzureReservations2ICS

python main.py your-azure-reservations-download-here.csv
```

## How to use

1. Download the Azure Portal CSV file on your Reservations page.
2. Run `python main.py wherever.csv`.
3. The ICal file will appear in that same directory as `wherever.ics`.
4. Import the ICS file to Outlook, Google Calendar, wherever you wish!

## Prerequisites

- `ics` (for handling the ICS stuff)
- `click` (for the CLI stuff)

This should work even if you have a very large amount of Azure reservations,
since Python's native `csv` file streams data as needed.

