# Using from module import Syntax

Python provides different ways to import components from modules. Let us explore the `from module import` syntax.

1. Restart the Python interpreter to get a clean state:

```python
>>> exit()
```

```bash
python3
```

2. Import specific components from a module using the `from module import` syntax:

```python
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
```

Notice that even though you only imported the `foo` function, the entire module was loaded (as evidenced by the "Loaded simplemod" output).

3. When using `from module import`, you cannot access the module itself:

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
```

4. You can import multiple components at once:

```python
>>> from simplemod import x, foo
>>> x
42
>>> foo()
x is 42
```

5. When you import a variable from a module, you are creating a new reference to the object, not a link to the variable in the module:

```python
>>> x = 13  # Change the local variable x
>>> x
13
>>> foo()
x is 42  # The function still uses the module's x, not your local x
```

The function `foo()` still refers to the module's variable `x`, not the local variable you changed. This is important to understand to avoid confusion in your code.
