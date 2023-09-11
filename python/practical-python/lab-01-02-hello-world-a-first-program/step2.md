# Interactive Mode

When you start Python, you get an _interactive_ mode where you can experiment.

If you start typing statements, they will run immediately. There is no edit/compile/run/debug cycle.

```python
>>> print('hello world')
hello world
>>> 37*42
1554
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
>>>
```

This so-called _read-eval-print-loop_ (or REPL) is very useful for debugging and exploration.

**STOP**: If you can't figure out how to interact with Python, stop what you're doing and figure out how to do it. If you're using an IDE, it might be hidden behind a menu option or other window. Many parts of this course assume that you can interact with the interpreter.

Let's take a closer look at the elements of the REPL:

- `>>>` is the interpreter prompt for starting a new statement.
- `...` is the interpreter prompt for continuing a statement. Enter a blank line to finish typing and run what you've entered.

The `...` prompt may or may not be shown depending on your environment. For this course, it is shown as blanks to make it easier to cut/paste code samples.

The underscore `_` holds the last result.

```python
>>> 37 * 42
1554
>>> _ * 2
3108
>>> _ + 50
3158
>>>
```

_This is only true in the interactive mode._ You never use `_` in a program.

