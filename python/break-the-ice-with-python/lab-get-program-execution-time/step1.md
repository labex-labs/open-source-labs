# Get Program Execution Time

Please write a program to print the running time of execution of "1+1" for 10000000 times.

## Preparation

Before we start writing the code, we should open the `/home/labex/project/get_program_execution_time.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
import time


def get_program_execution_time():
    before = time.time()
    for i in range(10000000):
        x = 1 + 1
    after = time.time()
    execution_time = after - before
    print(execution_time)


get_program_execution_time()

```

This Python code defines a function called `get_program_execution_time`. Within the function, the `time` module is imported.

The `time.time()` function is used to record the current time before and after a loop that performs a simple addition operation 10 million times.

The difference between the two recorded times is then calculated to determine the execution time of the loop.

Finally, the execution time is printed to the console using the `print` function.

Overall, this code demonstrates how to use the `time` module in Python to measure the execution time of a program or a specific section of code.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/get_program_execution_time.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

The output of the program may be:

```bash
0.37961649894714355
```

At this point, your code is running successfully!
