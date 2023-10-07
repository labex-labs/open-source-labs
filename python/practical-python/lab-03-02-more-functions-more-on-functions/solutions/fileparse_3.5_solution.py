# fileparse_3.5.py

import csv


def parse_csv(filename, select=None, types=None):
    """
    Parse a CSV file into a list of records
    """
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:  # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Apply type conversions if specified
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)

    return records


# Read all of the data with type conversions
portfolio = parse_csv("/home/labex/project/portfolio.csv", types=[str, int, float])
print(portfolio)

# Read only some of the data with type conversions
shares_held = parse_csv(
    "/home/labex/project/portfolio.csv", select=["name", "shares"], types=[str, int]
)
print(shares_held)
