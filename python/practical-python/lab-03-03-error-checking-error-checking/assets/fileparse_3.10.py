# fileparse_3.10.py
import csv

def parse_csv(filename, select=None, types=None, has_headers=True):
    '''
    Parse a CSV file into a list of dictionaries
    '''
    

portfolio = parse_csv('/home/labex/project/missing.csv', types=[str, int, float], silence_errors=True)
print(portfolio)