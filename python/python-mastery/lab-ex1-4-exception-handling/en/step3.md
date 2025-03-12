# Interactive Experimentation

Python allows you to run code in an interactive mode, which is excellent for testing and experimentation. In this step, you'll learn how to call your function directly from the Python interpreter.

## Running Python in Interactive Mode

You can run a Python script and then drop into interactive mode by using the `-i` flag:

```bash
cd /home/labex/project
python3 -i pcost.py
```

This command:

1. Executes the `pcost.py` script
2. Keeps Python running in interactive mode
3. Allows you to type Python commands directly into the terminal

You'll see the script's output followed by the Python prompt (`>>>`).

## Calling Your Function Interactively

Once in interactive mode, you can call the `portfolio_cost()` function with different filenames:

```python
>>> portfolio_cost('/home/labex/project/portfolio.dat')
44671.15
>>> portfolio_cost('/home/labex/project/portfolio2.dat')
19908.75
>>> portfolio_cost('/home/labex/project/portfolio3.dat')
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

This interactive approach allows you to:

- Test your function with different inputs
- Experiment with the function's behavior
- Debug your code on the fly

## Benefits of Interactive Mode

Interactive mode is beneficial because:

1. You can quickly test different scenarios
2. You can inspect variables and expression results immediately
3. You can test small pieces of code without creating a full program
4. It's great for learning and experimentation

## Exiting Interactive Mode

When you're done experimenting, you can exit the interactive mode by:

- Typing `exit()` and pressing Enter
- Pressing Ctrl+D (on Unix/Linux)

Throughout your Python programming journey, this technique of defining functions and testing them interactively will be extremely valuable for development and debugging.
