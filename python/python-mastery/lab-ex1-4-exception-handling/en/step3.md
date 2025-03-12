# Interactive Experimentation

Python offers an interactive mode that lets you run code right away. This is super useful for testing out your code and trying new things. In this step, we'll learn how to call a function directly from the Python interpreter.

## Running Python in Interactive Mode

To run a Python script and then enter the interactive mode, you can use the `-i` flag. This flag tells Python to keep running in an interactive state after executing the script. Here's how you do it:

```bash
cd /home/labex/project
python3 -i pcost.py
```

Let's break down what this command does:

1. First, `cd /home/labex/project` changes the current directory to `/home/labex/project`. This is where our `pcost.py` script is located.
2. Then, `python3 -i pcost.py` executes the `pcost.py` script. After the script finishes running, Python stays in interactive mode.
3. In interactive mode, you can type Python commands directly into the terminal.

After running the command, you'll see the output of the `pcost.py` script, followed by the Python prompt (`>>>`). This prompt indicates that you can now enter Python commands.

## Calling Your Function Interactively

Once you're in the interactive mode, you can call the `portfolio_cost()` function with different filenames. This allows you to see how the function behaves with various inputs. Here's an example:

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

Using this interactive approach, you can:

- Test your function with different inputs to see if it works as expected.
- Experiment with the function's behavior under various conditions.
- Debug your code on the fly by seeing the immediate results of your function calls.

## Benefits of Interactive Mode

Interactive mode has several benefits:

1. You can quickly test different scenarios without having to run the entire script every time.
2. You can inspect variables and expression results immediately, which helps you understand what's going on in your code.
3. You can test small pieces of code without creating a full program. This is great for learning and trying out new ideas.
4. It's an excellent way to learn and experiment with Python because you get instant feedback.

## Exiting Interactive Mode

When you're done experimenting, you can exit the interactive mode in two ways:

- Type `exit()` and press Enter. This is a straightforward way to end the interactive session.
- Press Ctrl+D (on Unix/Linux). This is a shortcut that also exits the interactive mode.

Throughout your Python programming journey, the technique of defining functions and testing them interactively will be extremely valuable for development and debugging. It allows you to quickly iterate on your code and find and fix issues.
