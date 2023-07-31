# Use of Digit Binary Numbers

Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/use_of_digit_binary_numbers.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def use_of_digit_binary_numbers():
    data = input().split(',')
    data = [num for num in data if int(num, 2) % 5 == 0]
    print(','.join(data))


use_of_digit_binary_numbers()

```

This Python code defines a function called `use_of_digit_binary_numbers()` that filters a list of binary numbers to only include those that are divisible by 5 when converted to decimal. The function prompts the user to input a comma-separated list of binary numbers using the `input()` function and splits it into a list using the `split()` function.

The function then uses a list comprehension to iterate over each number `num` in the list and checks if it is divisible by 5 when converted to decimal using the `int()` function with a base of 2. If the number is divisible by 5, it is included in the new list.

Finally, the function uses the `join()` method to concatenate the filtered list of binary numbers into a comma-separated string and prints it to the console using the `print()` function.

The `use_of_digit_binary_numbers()` function is then called to execute it and prompt the user for input.

Overall, this code demonstrates how to filter a list of binary numbers in Python based on a condition using a list comprehension and the `int()` function with a base of 2 to convert binary to decimal. It also shows how to use the `join()` method to concatenate a list into a string with a specified separator.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/use_of_digit_binary_numbers.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
0100,0011,1010,1001
```

Then, the output of the program should be:

```bash
1010
```

At this point, your code is running successfully!
