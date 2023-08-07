# reader.py

import csv


def convert_csv(lines, converter, *, headers=None):
    records = []
    rows = csv.reader(lines)
    if headers is None:
        headers = next(rows)
    return map(lambda row: converter(headers, row), rows)
