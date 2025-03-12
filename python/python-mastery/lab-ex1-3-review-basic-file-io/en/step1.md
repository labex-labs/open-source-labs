# Understanding the Problem

In this step, we'll first understand what the problem we need to solve is and then take a look at the data we'll be working with. This is an important first step in any programming task because it helps us know exactly what we're aiming for and what resources we have at our disposal.

In your project directory, there's a file named `portfolio.dat`. This file stores information about a portfolio of stocks. A portfolio is like a collection of different stocks that an investor owns. Each line in this file represents a single stock purchase. The format of each line is as follows:

```
[Stock Symbol] [Number of Shares] [Price per Share]
```

The stock symbol is a short code that represents a particular company's stock. The number of shares tells us how many units of that stock were bought, and the price per share is the cost of one unit of that stock.

Let's take a look at an example. Consider the first line of the file:

```
AA 100 32.20
```

This line indicates that 100 shares of the stock with the symbol "AA" were purchased. Each share cost $32.20.

If you want to see what's inside the `portfolio.dat` file, you can run the following command in the terminal. The `cat` command is a useful tool in the terminal that allows you to view the contents of a file.

```bash
cat ~/project/portfolio.dat
```

Now, your task is to create a Python program named `pcost.py`. This program will perform three main tasks:

1. First, it needs to open and read the `portfolio.dat` file. Opening a file in Python allows our program to access the data stored inside it.
2. Then, it has to calculate the total cost of all the stock purchases in the portfolio. To do this, for each line in the file, we need to multiply the number of shares by the price per share. After getting these values for each line, we sum them all up. This gives us the total amount of money spent on all the stocks in the portfolio.
3. Finally, the program should output the total cost. This way, we can see the result of our calculations.

Let's begin by creating the `pcost.py` file. You can use the editor to open and edit this file. It was already created for you during the setup step. This file will be the place where you write the Python code to solve the problem we just discussed.
