# fileparse_3.8.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True):
    '''
    Parse a CSV file into a list of dictionaries
    '''
    if select and not has_headers:
        raise RuntimeError("select argument requires column headers")

    with open(filename) as f:
        rows = csv.reader(f)

        # Skip the header row if present
        if has_headers:
            headers = next(rows)
        else:
            headers = []

        # If a column selector was given, find indices of the specified columns.
        # Also narrow the set of headers used for resulting dictionaries
        if select:
            indices = [headers.index(colname) for colname in select]
            headers = select
        else:
            indices = []

        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Apply type conversions if specified
            if types:
                row = [func(val) for func, val in zip(types, row)]

            # Make a dictionary with the specified order of fields
            record = dict(zip(headers, row))
            records.append(record)

    return records

parse_csv('/home/labex/project/prices.csv', select=['name', 'price'], has_headers=False)
