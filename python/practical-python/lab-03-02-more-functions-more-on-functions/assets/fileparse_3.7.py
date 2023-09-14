# fileparse_3.7.py

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records
    '''
    

# Read all of the data with a different delimiter
portfolio = parse_csv('/home/labex/project/portfolio.dat', types=[str, int, float], delimiter=' ')
print(portfolio)