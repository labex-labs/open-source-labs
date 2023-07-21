# Define a Class

Define a class which has at least two methods:

- getString: to get a string from console input.
- printString: to print the string in upper case.

Also please include simple test function to test the class methods.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/define_a_class.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
class IOstring():
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input()

    def print_string(self):
        print(self.s.upper())


xx = IOstring()
xx.get_string()
xx.print_string()

```

This Python code defines a class called `IOstring`, which contains two methods: `get_string` and `print_string`. The class's constructor initializes an empty string variable called `s`.

The `get_string` method uses the `input` function to read a user-input string from the console and stores it in the instance variable `s`.

The `print_string` method converts the string in the instance variable `s` to uppercase letters and uses the `print` function to output it to the console.

In the main program, an instance of the `IOstring` class called `xx` is created, and the `get_string` and `print_string` methods are called in to obtain the user-input string and output it in uppercase letters to the console.

Overall, this code demonstrates how to define a class and its methods to obtain and process user-input strings. It also shows how to use an instance of the class to call these methods and output the processed result to the console.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/define_a_class.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Suppose the following input is supplied to the program:

```bash
hello python!
```

Then, the output of the program should be:

```bash
HELLO PYTHON!
```

At this point, your code is running successfully!
