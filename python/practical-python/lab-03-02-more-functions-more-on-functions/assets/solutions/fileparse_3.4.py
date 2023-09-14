# fileparse_3.4.py
import csv

def parse_csv(filename, select=None):
    '''
    Parse a CSV file into a list of records
    '''
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
            if not row:    # Skip rows with no data
                continue
            # Filter the row if specific columns were selected
            if indices:
                row = [row[index] for index in indices]

            # Make a dictionary
            record = dict(zip(headers, row))
            records.append(record)

    return records


# Run the parse_csv function with /home/labex/project/portfolio.csv
# Read all of the data
portfolio = parse_csv('/home/labex/project/portfolio.csv')
print(portfolio)

# Read only some of the data
shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name', 'shares'])
print(shares_held)