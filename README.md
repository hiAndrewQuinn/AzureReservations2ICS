Azure Reservation CSV to `.ics` / ICal file
==================================

A tiny CSV to ICS wrapper that can save you a lot of money.

## Quickstart

```bash
pip install ics      # for the ics / ical parser
pip install click    # for the very tiny cli

git clone https://github.com/hiAndrewQuinn/AzureReservations2ICS.git
cd AzureReservations2ICS

python main.py --help
```

## How to use

1. Download the Azure Portal CSV file on your Reservations page.
2. Run `python main.py wherever.csv`.
3. The ICal file will appear in that same directory as `wherever.ics`.
4. Import the ICS file to Outlook, Google Calendar, wherever you wish!

This should work even if you have a very large amount of Azure reservations,
since Python's native `csv` file just streams data as needed.
