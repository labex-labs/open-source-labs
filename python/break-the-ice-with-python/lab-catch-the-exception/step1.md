# Catching the Exception

Write a function to compute 5/0 and use `try/except` to catch the exceptions.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/catch_the_exception.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def divide():
    return 5 / 0


try:
    divide()
except ZeroDivisionError as ze:
    print("Why on earth you are dividing a number by ZERO!!")
except:
    print("Any other exception")

```

This Python code defines a function called `divide` that attempts to divide the number 5 by 0, which raises a `ZeroDivisionError` exception. It uses a `try` block to call the `divide` function and prints error message if a `ZeroDivisionError` exception occurs. If any other type of exception occurs, it prints a different error message.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/catch_the_exception.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
Why on earth you are dividing a number by ZERO!!
```

At this point, your code is running successfully!
