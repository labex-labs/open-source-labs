# Using from module import Syntax

In Python, there are various ways to import components from modules. One of these ways is the `from module import` syntax, which we'll explore in this section.

When you import components from a module, it's often a good idea to start with a clean slate. This ensures that there are no leftover variables or settings from previous interactions that could interfere with our current experiment.

1. Restart the Python interpreter to get a clean state:

```python
>>> exit()
```

This command exits the current Python interpreter session. After exiting, we'll start a new session to ensure a fresh environment.

```bash
python3
```

This bash command starts a new Python 3 interpreter session. Now that we have a clean Python environment, we can start importing components from a module.

2. Import specific components from a module using the `from module import` syntax:

```python
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
```

Here, we're using the `from simplemod import foo` statement to import only the `foo` function from the `simplemod` module. Notice that even though we only asked for the `foo` function, the entire `simplemod` module was loaded. This is indicated by the "Loaded simplemod" output. The reason for this is that Python needs to load the whole module to access the `foo` function.

3. When using `from module import`, you cannot access the module itself:

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
```

When we use the `from module import` syntax, we're only bringing in the specified components directly into our namespace. The module name itself is not imported. So, when we try to access `simplemod.foo()`, Python doesn't recognize `simplemod` because it wasn't imported in that way.

4. You can import multiple components at once:

```python
>>> from simplemod import x, foo
>>> x
42
>>> foo()
x is 42
```

The `from module import` syntax allows us to import multiple components from a module in a single statement. Here, we're importing both the variable `x` and the function `foo` from the `simplemod` module. After importing, we can directly access these components in our code.

5. When you import a variable from a module, you are creating a new reference to the object, not a link to the variable in the module:

```python
>>> x = 13  # Change the local variable x
>>> x
13
>>> foo()
x is 42  # The function still uses the module's x, not your local x
```

When we import a variable from a module, we're essentially creating a new reference to the same object in our local namespace. So, when we change the local variable `x` to `13`, it doesn't affect the `x` variable inside the `simplemod` module. The `foo()` function still refers to the module's `x` variable, which is `42`. Understanding this concept is crucial to avoid confusion in your code.
