# fileparse_3.5.py

def parse_csv(filename):
    '''
    Parse a CSV file into a list of records
    '''
    

# Read all of the data with type conversions
portfolio = parse_csv('/home/labex/project/portfolio.csv', types=[str, float, int])
print(portfolio)

# Read only some of the data with type conversions
shares_held = parse_csv('/home/labex/project/portfolio.csv', select=['name', 'shares'], types=[str, int])
print(shares_held)