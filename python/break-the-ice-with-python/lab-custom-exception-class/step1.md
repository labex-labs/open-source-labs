# Custom Exception Class

Define a custom exception class which takes a string message as attribute.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/custom_exception_class.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
class CustomException(Exception):

    def __init__(self, message):
        self.message = message


num = int(input())

try:
    if num < 10:
        raise CustomException("Input is less than 10")
    elif num > 10:
        raise CustomException("Input is grater than 10")
except CustomException as ce:
    print("The error raised: " + ce.message)

```

This Python code defines a custom exception class called `CustomException`, which inherits from Python's built-in `Exception` class. The class's constructor takes a string parameter `message` and stores it in an instance variable called `message`.

Next, the `input` function is used to read a user-input integer, which is stored in the variable `num`. Then, a `try` and `except` block is used to catch any potential custom exceptions.

Inside the `try` block, `if` and `elif` statements are used to check if the input integer is less than or greater than 10. If the input integer is less than 10, a custom exception is raised using the `raise` statement, with its message set to "Input is less than 10". If the input integer is greater than 10, another custom exception is raised with its message set to "Input is greater than 10".

Inside the `except` block, the custom exception is caught and its message is printed to the console using the `print` function.

Overall, this code demonstrates how to define and use a custom exception class to handle specific error cases.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/custom_exception_class.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following string is given as input to the program:

```bash
5
```

Then, the output of the program should be:

```bash
The error raised: Input is less than 10
```

At this point, your code is running successfully!
