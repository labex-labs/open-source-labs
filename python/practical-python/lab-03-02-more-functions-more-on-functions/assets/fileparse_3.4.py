def parse_csv(filename):
    """
    Parse a CSV file into a list of records
    """


# Run the parse_csv function with /home/labex/project/portfolio.csv
# Read all of the data
portfolio = parse_csv("/home/labex/project/portfolio.csv")
print(portfolio)

# Read only some of the data
shares_held = parse_csv("/home/labex/project/portfolio.csv", select=["name", "shares"])
print(shares_held)
