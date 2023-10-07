# pcost.py

import report


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)
    return sum([s["shares"] * s["price"] for s in portfolio])
