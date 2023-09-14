# fileparse_3.3.py
import csv

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records
    '''
    with open(filename) as f:
        rows = csv.reader(f)

        # Read the file headers
        headers = next(rows)
        records = []
        for row in rows:
            if not row:    # Skip rows with no data
                continue
            record = dict(zip(headers, row))
            records.append(record)

    return records


# Run the parse_csv function with portfolio.csv
portfolio = parse_csv('/home/labex/project/portfolio.csv')
print(portfolio)