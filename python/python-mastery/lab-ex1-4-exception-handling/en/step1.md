# Defining a Function

In this step, we're going to learn how to create a function. A function in Python is a block of organized, reusable code that is used to perform a single, related action. Here, our function will read portfolio data from a file and calculate the total cost. This is useful because once we have this function, we can use it multiple times with different portfolio files, saving us from writing the same code over and over again.

## Understanding the Problem

In the previous lab, you might have written some code to read portfolio data and calculate the total cost. But that code was probably written in a way that can't be easily reused. Now, we're going to convert that code into a reusable function.

The portfolio data files have a specific format. They contain information in the form of "Symbol Shares Price". Each line in the file represents a stock holding. For example, in a file named `portfolio.dat`, you might see lines like this:

```
AA 100 32.20
IBM 50 91.10
...
```

Here, the first part (like "AA" or "IBM") is the stock symbol, which is a unique identifier for the stock. The second part is the number of shares you own of that stock, and the third part is the price per share.

## Creating the Function

Let's create a Python file called `pcost.py` in the `/home/labex/project` directory. This file will contain our function. Here's the code that we'll put in the `pcost.py` file:

```python
def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file

    Args:
        filename: The name of the portfolio file

    Returns:
        The total cost of the portfolio as a float
    """
    total_cost = 0.0

    # Open the file and read through each line
    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            # Extract the data (symbol, shares, price)
            shares = int(fields[1])
            price = float(fields[2])
            # Add the cost to our running total
            total_cost += shares * price

    return total_cost

# Call the function with the portfolio.dat file
if __name__ == '__main__':
    cost = portfolio_cost('/home/labex/project/portfolio.dat')
    print(cost)
```

In this code, we first define a function named `portfolio_cost` that takes a `filename` as an argument. Inside the function, we initialize a variable `total_cost` to 0.0. Then we open the file using the `open` function in read mode (`'r'`). We use a `for` loop to go through each line in the file. For each line, we split it into fields using the `split()` method. We then extract the number of shares and convert it to an integer, and the price and convert it to a float. We calculate the cost for that stock holding by multiplying the number of shares by the price and add it to the `total_cost`. Finally, we return the `total_cost`.

The part `if __name__ == '__main__':` is used to call the function when the script is run directly. We pass the path to the `portfolio.dat` file to the function and print the result.

## Testing the Function

Now, let's run the program to see if it works. We need to navigate to the directory where the `pcost.py` file is located and then run the Python script. Here are the commands to do that:

```bash
cd /home/labex/project
python3 pcost.py
```

After running these commands, you should see the output:

```
44671.15
```

This output represents the total cost of all the stocks in the portfolio.

## Understanding the Code

Let's break down what our function does step by step:

1. It takes a `filename` as an input parameter. This allows us to use the function with different portfolio files.
2. It opens the file and reads it line by line. This is done using the `open` function and a `for` loop.
3. For each line, it splits the line into fields using the `split()` method. This method splits the line into a list of strings based on whitespace.
4. It converts the number of shares to an integer and the price to a float. This is necessary because the data read from the file is in string format, and we need to perform arithmetic operations on them.
5. It calculates the cost (shares \* price) for each stock holding and adds it to the running total. This gives us the total cost of the portfolio.
6. It returns the final total cost. This allows us to use the result in other parts of our program if needed.

This function is now reusable. We can call it with different portfolio files to calculate their costs, which makes our code more efficient and easier to maintain.
