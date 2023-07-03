# Counting Characters in Strings

Please write a program which count and print the numbers of each character in a string input by console.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/counting_characters_in_strings.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import string


def counting_characters_in_strings():
    s = input()
    for letter in string.ascii_lowercase:
        cnt = s.count(letter)
        if cnt > 0:
            print("{},{}".format(letter, cnt))


counting_characters_in_strings()

```

This Python code defines a function called `counting_characters_in_strings` that takes a user-input string and counts the occurrences of each lowercase letter in the string.

Inside the function, the `input` function is used to read the user's input string, and `string.ascii_lowercase` is used to obtain a list of all lowercase letters. Then, a `for` loop is used to iterate over each lowercase letter, and the `count` function is used to count the number of times that letter appears in the input string. If the count is greater than 0, the `print` function is used to format the letter and count as a string and output it to the console.

Overall, this code demonstrates how to define a function and use it to count the occurrences of each lowercase letter in a user-input string.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/counting_characters_in_strings.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following string is given as input to the program:

```bash
abcdefgabc
```

Then, the output of the program should be:

```bash
a,2
c,2
b,2
e,1
d,1
g,1
f,1
```

At this point, your code is running successfully!
