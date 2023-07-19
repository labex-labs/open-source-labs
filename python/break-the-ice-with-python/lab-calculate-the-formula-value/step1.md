# Calculate the Formula Value

Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/calculate_the_formula_value.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def calculate_the_formula_value():
    a = input()
    total = int(a) + int(2*a) + int(3*a) + int(4*a)
    print(total)


calculate_the_formula_value()

```

This code implements a function `calculate_the_formula_value` to calculate the value of a number four times plus three times, twice and double and print the result to the console. It uses the `input()` function to read the number entered by the user and converts it to an integer type using the `int()` function. It then calculates the value of quadruple plus triple, double and double and stores the result in a variable. Finally, the result of the calculation is printed to the console.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/calculate_the_formula_value.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
9
```

Then, the output of the program should be:

```bash
11106
```

At this point, your code is running successfully!
