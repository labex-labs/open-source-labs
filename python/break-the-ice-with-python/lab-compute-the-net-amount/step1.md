# Compute the Net Amount

Write a program that computes the net amount of a bank account based a transaction log from console input.

The transaction log format is shown as following:

```bash
D 100
W 200
```

- D means deposit while W means withdrawal.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/compute_the_net_amount.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def compute_the_net_amount():
    total = 0
    while True:
        s = input().split()
        if not s:            # break if the string is empty
            break
        # two inputs are distributed in cm and num in string data type
        cm, num = map(str, s)

        if cm == 'D':
            total += int(num)
        if cm == 'W':
            total -= int(num)

    print(total)


compute_the_net_amount()

```

This Python code demonstrates how to calculate the net amount of a bank account. First, a function named `compute_the_net_amount` is defined, which initializes a variable `total` to 0.

Next, an infinite loop is used to read user input commands until an empty line is entered. Each command is a string consisting of two parts: a letter and a number, separated by a space. Depending on the letter, the number is added to or subtracted from `total`, simulating deposits and withdrawals from the bank account.

Finally, the `print` function is used to print the calculated net amount to the console.

Overall, this code demonstrates how to use loops and conditional statements to simulate deposits and withdrawals from a bank account, and calculate the net amount of the account.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/compute_the_net_amount.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
D 300
D 300
W 200
D 100
```

Then, the output of the program should be:

```bash
500
```

At this point, your code is running successfully!
