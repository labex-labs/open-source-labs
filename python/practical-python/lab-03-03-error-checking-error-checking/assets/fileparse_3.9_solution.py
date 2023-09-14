# fileparse_3.9.py
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
        for row_num, row in enumerate(rows, start=1):
            if not row:    # Skip rows with no data
                continue
            try:
                # Filter the row if specific columns were selected
                if indices:
                    row = [row[index] for index in indices]

                # Apply type conversions if specified
                if types:
                    row = [func(val) for func, val in zip(types, row)]

                # Make a dictionary with the specified order of fields
                record = dict(zip(headers, row))
                records.append(record)
            except ValueError as e:
                print(f"Row {row_num}: Couldn't convert {row}")
                print(f"Row {row_num}: Reason {str(e)}")

    return records


portfolio = parse_csv('/home/labex/project/missing.csv', types=[str, int, float])