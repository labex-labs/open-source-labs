# Launch Python Interactive Interpreter

The Python interactive interpreter allows you to type Python code directly and see immediate results. It is an excellent tool for learning Python, testing small code snippets, and exploring Python features.

## Launch the Python Interpreter

1. Open a terminal in your LabEx environment.

2. Start the Python interpreter by typing the following command:

   ```bash
   python3
   ```

3. You should see something similar to this:

   ```
   Python 3.10.x (default, ...)
   [GCC x.x.x] on linux
   Type "help", "copyright", "credits" or "license" for more information.
   >>>
   ```

   The `>>>` prompt indicates that Python is waiting for your input.

## Try a Simple Command

Let's write our first Python code. Type the following at the prompt:

```python
>>> print('Hello World')
```

After pressing Enter, you should see:

```
Hello World
>>>
```

This confirms that Python is running correctly. The `print()` function outputs text to the screen.

## Exit the Interpreter

When you're done experimenting with the Python interpreter, you can exit by:

1. Typing `exit()` or `quit()` and pressing Enter, or
2. Pressing Ctrl+D on your keyboard

```python
>>> exit()
```

The interactive interpreter is called a REPL (Read-Evaluate-Print Loop) because it:

- Reads your input
- Evaluates (runs) your code
- Prints the result
- Loops back to wait for more input
