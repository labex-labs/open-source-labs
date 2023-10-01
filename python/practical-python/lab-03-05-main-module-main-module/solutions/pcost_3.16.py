#!/usr/bin/env python3
# pcost.py
import sys


sys.path.append('/home/labex/project')

import report


def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    portfolio = report.read_portfolio(filename)
    return sum([s["shares"] * s["price"] for s in portfolio])


def main(args):
    if len(args) != 2:
        raise SystemExit("Usage: %s portfoliofile" % args[0])
    filename = args[1]
    print("Total cost:", portfolio_cost(filename))


if __name__ == "__main__":

    main(sys.argv)
