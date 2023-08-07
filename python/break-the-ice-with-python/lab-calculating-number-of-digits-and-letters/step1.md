# Calculating Number of Digits and Letters

Write a Python program that accepts a string and calculate the number of digits and letters.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/calculating_number_of_digits_and_letters.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def calculating_number_of_digits_and_letters():
    word = input()
    digit, letter = 0, 0
    for char in word:
        digit += char.isdigit()
        letter += char.isalpha()

    print('Digit -', digit)
    print('Letter -', letter)


calculating_number_of_digits_and_letters()

```

This Python code defines a function called `calculating_number_of_digits_and_letters` that calculates the number of digits and letters in an input string and prints the results to the console. It uses two variables, `digit` and `letter`, to store the number of digits and letters, and iterates through each character in the string using the `isdigit()` and `isalpha()` methods to determine if the character is a digit or letter. Finally, it prints the number of digits and letters to the console.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/calculating_number_of_digits_and_letters.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following string is given as input to the program:

```bash
Hello321Bye360
```

Then, the output of the program should be:

```bash
Digit - 6
Letter - 8
```

At this point, your code is running successfully!
