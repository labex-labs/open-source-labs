# Working with files

The file `portfolio.dat` contains a list of lines with information on a portfolio of stocks. The file looks like this:

    AA 100 32.20
    IBM 50 91.10
    CAT 150 83.44
    MSFT 200 51.23
    GE 95 40.37
    MSFT 50 65.10
    IBM 100 70.44

The first column is the stock name, the second column is the number of shares, and the third column is the purchase price of a single share.

Write a program called `pcost.py` that opens this file, reads all lines, and calculates how much it cost to purchase all of the shares in the portfolio. To do this, compute the sum of the second column multiplied by the third column. Finally, output the results of the calculation.
