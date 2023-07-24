# Assert Expression

Please write assert statements to verify that every number in the list [2,4,5,6] is even.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/assert_expression.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
data = [2, 4, 5, 6]
for i in data:
    assert i % 2 == 0, "{} is not an even number".format(i)

```

This Python code ensures that all elements in the `data` list are even numbers. If any odd numbers are present, an `AssertionError` is raised by `assert` statements with a message indicating which number is not even.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/assert_expression.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

Then, the output of the program should be:

```bash
AssertionError: 5 is not an even number
```

At this point, your code is running successfully!
