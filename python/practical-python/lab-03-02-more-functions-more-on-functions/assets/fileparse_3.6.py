# fileparse_3.6.py


def parse_csv(filename):
    """
    Parse a CSV file into a list of records
    """


# Read all of the data without headers
prices = parse_csv(
    "/home/labex/project/prices.csv", types=[str, float], has_headers=False
)
print(prices)
