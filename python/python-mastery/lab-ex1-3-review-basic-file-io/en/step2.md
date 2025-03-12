# Opening and Reading the File

In this step, we're going to learn how to open and read a file in Python. File input/output (I/O) is a fundamental concept in programming. It allows your program to interact with external files, like text files, CSV files, and more. In Python, one of the most common ways to work with files is by using the `open()` function.

The `open()` function is used to open a file in Python. It takes two important arguments. The first argument is the name of the file you want to open. The second argument is the mode in which you want to open the file. When you want to read a file, you use the mode 'r'. This tells Python that you only want to read the contents of the file and not make any changes to it.

Now, let's add some code to the `pcost.py` file to open and read the `portfolio.dat` file. Open the `pcost.py` file in your code editor and add the following code:

```python
# pcost.py
# Calculate the total cost of a portfolio of stocks

def portfolio_cost(filename):
    """
    Computes the total cost (shares*price) of a portfolio file
    """
    total_cost = 0.0

    # Open the file
    with open(filename, 'r') as file:
        # Read all lines in the file
        for line in file:
            print(line)  # Just for debugging, to see what we're reading

    # Return the total cost
    return total_cost

# Call the function with the portfolio file
total_cost = portfolio_cost('portfolio.dat')
print(f'Total cost: ${total_cost}')
```

Let's break down what this code does:

1. First, we define a function named `portfolio_cost()`. This function takes a filename as an input parameter. The purpose of this function is to calculate the total cost of a portfolio of stocks based on the data in the file.
2. Inside the function, we use the `open()` function to open the specified file in read mode. The `with` statement is used here to ensure that the file is properly closed after we're done reading it. This is a good practice to avoid resource leaks.
3. We then use a `for` loop to read the file line by line. For each line in the file, we print it. This is just for debugging purposes, so we can see what data we're reading from the file.
4. After reading the file, the function returns the total cost. Currently, the total cost is set to 0.0 because we haven't implemented the actual calculation yet.
5. Outside the function, we call the `portfolio_cost()` function with the filename 'portfolio.dat'. This means we're asking the function to calculate the total cost based on the data in the `portfolio.dat` file.
6. Finally, we print the total cost using an f-string.

Now, let's run this code to see what it does. You can run the Python file from the terminal using the following command:

```bash
python3 ~/project/pcost.py
```

When you run this command, you should see each line of the `portfolio.dat` file printed on the terminal, followed by the total cost, which is currently set to 0.0. This output helps you verify that the file is being read correctly.
