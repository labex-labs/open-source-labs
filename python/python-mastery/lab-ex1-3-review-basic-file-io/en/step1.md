# Understanding the Problem

In this step, we will understand the problem statement and examine the data we need to process.

The file `portfolio.dat` has been created in your project directory. This file contains information about a portfolio of stocks. Each line in the file represents a single stock purchase with the following format:

```
[Stock Symbol] [Number of Shares] [Price per Share]
```

For example, let's look at the first line:

```
AA 100 32.20
```

This means 100 shares of stock "AA" were purchased at a price of $32.20 per share.

You can view the contents of the file by running the following command in the terminal:

```bash
cat ~/project/portfolio.dat
```

Your task is to create a Python program called `pcost.py` that:

1. Opens and reads the `portfolio.dat` file
2. Calculates the total cost of all stock purchases in the portfolio
3. Outputs the total cost

To calculate the total cost, you need to multiply the number of shares by the price per share for each line, and then sum all these values.

Let's start by creating the `pcost.py` file. You can use the editor to open and edit this file, which was already created for you in the setup step.
