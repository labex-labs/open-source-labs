# Capitalize Characters

Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/capitalize_characters.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def capitalize_characters():
    lst = []

    while True:
        x = input()
        if len(x) == 0:
            break
        lst.append(x.upper())

    for line in lst:
        print(line)


capitalize_characters()

```

This Python code defines a function called `capitalize_characters` that converts user input strings to uppercase and prints the results to the console. It uses an infinite loop to get user input strings, converts them to uppercase using the `upper()` method, and appends them to a list called `lst`. Finally, it iterates through the `lst` list and prints each string to the console.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/capitalize_characters.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
Hello world
Practice makes perfect
```

Then, the output of the program should be:

```bash
HELLO WORLD
PRACTICE MAKES PERFECT
```

At this point, your code is running successfully!
