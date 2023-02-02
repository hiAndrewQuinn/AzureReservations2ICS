Azure Reservation CSV to `.ics` / ICal file
==================================

An issue came up with a customer recently where we keep forgetting
to book our Azure reservations, so I decided to write this little
CSV to ICS wrapper.

## Quickstart

```bash
pip install ics
pip install click
```

## How to use

1. Download the Azure Portal CSV file on your Reservations page.
2. Run `python main.py wherever.csv`.
3. The ICal file will appear in that same directory as `wherever.ics`.
4. Import it wherever you wish!

