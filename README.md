# Capital One Checking - Recurring expenses Python script 

A dead simple python script/CLI for parsing a CSV download from a
capitalone checking account.

At time of writing capital one allows you to download a transaction
history CSV file for up 2 previous years.

This tool takes that file and searches through that data and finds
recurring patterns in your expenses.

At the end of the script you are presented with a list of possible
recurring expenses, i.e. an old subscription that you may have forgotten
about.

Here is a demo of how it works:

[![asciicast](https://asciinema.org/a/409910.svg)](https://asciinema.org/a/409910)

# Instructions

```
$ git clone git@github.com:wgwz/capital-one-recurring-expenses.git
$ python3 -m venv venv
$ . venv/bin/activate
(venv) $ python setup.py install
(venv) $ python -m app <path-to-your-CSV-transaction-history>
```

# CSV Format

At time of writing the headers for this CSV are:

```
Account Number,Transaction Date,Transaction Amount,Transaction Type,Transaction Description,Balance
```

# Downloading the CSV

https://www.keepertax.com/posts/how-to-export-capital-one-bank-statements-as-a-spreadsheet-csv

# Note-to-self, making it distributable

```
(venv) $ pip install build
(venv) $ python -m build
```
