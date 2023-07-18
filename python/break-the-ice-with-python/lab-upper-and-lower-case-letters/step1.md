# Upper and Lower Case Letters

Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/upper_and_lower_case_letters.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def upper_and_lower_case_letters():
    word = input()
    # sum function cumulatively sum up 1's if the condition is True
    upper = sum(1 for i in word if i.isupper())
    lower = sum(1 for i in word if i.islower())

    print("UPPER CASE {0}\nLOWER CASE {1}".format(upper, lower))


upper_and_lower_case_letters()

```

This Python code defines a function called `upper_and_lower_case_letters()` that counts the number of uppercase and lowercase letters in a given string. The function prompts the user to input a string using the `input()` function and stores it in a variable called `word`.

The function then uses the `sum()` function and a generator expression to count the number of uppercase letters in the `word` string. The generator expression iterates over each character `i` in the `word` string and checks if it is uppercase using the `isupper()` method. If the character is uppercase, the generator expression returns `1`, which is then summed up by the `sum()` function.

The function then uses the `sum()` function and another generator expression to count the number of lowercase letters in the `word` string. The generator expression iterates over each character `i` in the `word` string and checks if it is lowercase using the `islower()` method. If the character is lowercase, the generator expression returns `1`, which is then summed up by the `sum()` function.

Finally, the function uses the `print()` function to output the number of uppercase and lowercase letters in the `word` string to the console in the format `"UPPER CASE {0}\nLOWER CASE {1}"`.

The `upper_and_lower_case_letters()` function is then called to execute it and prompt the user for input.

Overall, this code demonstrates how to count the number of uppercase and lowercase letters in a string using generator expressions and the `sum()` function in Python. It also shows how to use the `format()` method to format a string with variables.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/upper_and_lower_case_letters.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
Hello world!
```

Then, the output of the program should be:

```bash
UPPER CASE 1
LOWER CASE 9
```

At this point, your code is running successfully!
