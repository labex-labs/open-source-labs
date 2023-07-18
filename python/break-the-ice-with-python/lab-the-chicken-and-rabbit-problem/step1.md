# The Chicken and Rabbit Problem

Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

## Preparation

Before we start writing the code, we should open the `/home/labex/project/the_chicken_and_rabbit_problem.py` file in WebIDE.

## Start writing code

Then input the following code.

```python
def solve(numheads, numlegs):
    ns = 'No solutions!'
    for i in range(numheads+1):
        j = numheads-i
        if 2*i+4*j == numlegs:
            return i, j
    return ns, ns


numheads = 35
numlegs = 94
solutions = solve(numheads, numlegs)
print(solutions)

```

This Python code defines a function called `solve()` that solves a problem involving counting the number of chickens and rabbits given the number of heads and legs. The function takes two arguments `numheads` and `numlegs`, which represent the number of heads and legs, respectively.

The function initializes a variable called `ns` to the string `'No solutions!'`. It then uses a for loop to iterate over the range of numbers from `0` to `numheads+1`. For each number `i` in the range, the function calculates the number of rabbits `j` as `numheads-i`.

The function then checks if the total number of legs `2*i+4*j` is equal to `numlegs`. If it is, the function returns a tuple containing the number of chickens `i` and the number of rabbits `j`.

If no solution is found, the function returns the `ns` string twice.

The code then defines two variables `numheads` and `numlegs` and calls the `solve()` function with these variables as arguments. The resulting tuple is then printed to the console using the `print()` function.

Overall, this code demonstrates how to use a for loop and conditional statements to solve a problem involving counting the number of chickens and rabbits given the number of heads and legs in Python.

## Test your code

You can run the following command in the terminal to execute.

```bash
python3 /home/labex/project/the_chicken_and_rabbit_problem.py
```

Or you can just click the button like this ![Run Python File](./assets/run_python_file_button.jpg "Run Python File") in the top right corner to execute.

If We count 35 heads and 94 legs among the chickens and rabbits in a farm.

Then, the output of the program should be:

```bash
(23, 12)
```

At this point, your code is running successfully!
