# fileparse_3.8.py
import csv


def parse_csv(filename, select=None, types=None, has_headers=True):
    """
    Parse a CSV file into a list of dictionaries
    """


prices = parse_csv(
    "/home/labex/project/prices.csv", select=["name", "price"], has_headers=False
)
print(prices)
