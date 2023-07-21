# Calculate Mathematical Expression

Please write a program which accepts basic mathematic expression from console and print the evaluation result.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/calculate_mathematical_expression.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def calculate_mathematical_expression():
    expression = input()
    ans = eval(expression)
    print(ans)

    return ans


calculate_mathematical_expression()

```

This Python code implements a function called `calculate_mathematical_expression` that calculates the value of a mathematical expression entered by the user. It reads the expression from user input and uses the built-in `eval` function to evaluate the expression and store the result in a variable called `ans`. The function then prints the result to the console and returns it. The function is called at the end to calculate the value of the expression entered by the user.

Overall, this code provides a simple way to calculate the value of a mathematical expression entered by the user using Python's built-in `eval` function.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/calculate_mathematical_expression.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If the following basic mathematic expression is given as input to the program:

```bash
35 + 3
```

Then, the output of the program should be:

```bash
38
```

At this point, your code is running successfully!
