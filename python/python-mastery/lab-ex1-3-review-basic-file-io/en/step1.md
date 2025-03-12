# Understanding the Problem and File Structure

In this first step, we will understand the problem and examine the file structure we need to work with.

## The Portfolio Data File

The file `portfolio.dat` contains information about a portfolio of stocks. Each line in the file represents a stock holding with the following format:

1. The first column is the stock symbol (e.g., AA, IBM, MSFT)
2. The second column is the quantity of shares
3. The third column is the purchase price per share

Let's look at the contents of the file:

```bash
cat ~/project/portfolio.dat
```

You should see the following output:

```
AA 100 32.20
IBM 50 91.10
CAT 150 83.44
MSFT 200 51.23
GE 95 40.37
MSFT 50 65.10
IBM 100 70.44
```

## Our Task

We need to write a Python program called `pcost.py` that:

1. Opens and reads the `portfolio.dat` file
2. For each line, multiplies the number of shares by the price per share
3. Calculates the sum of these products to find the total cost of the portfolio
4. Outputs the result

Let's proceed to create the Python program in the next step.
