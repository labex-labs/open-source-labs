# Exploring Module Reloading Limitations

Module reloading has some limitations, especially when working with classes. Let us explore these limitations.

1. Restart the Python interpreter:

```python
>>> exit()
```

```bash
python3
```

2. Import the module and create an instance of the `Spam` class:

```python
>>> import simplemod
Loaded simplemod
>>> s = simplemod.Spam()
>>> s.yow()
Yow!
```

3. Now let us modify the `Spam` class in our module. Exit the Python interpreter:

```python
>>> exit()
```

4. Open the `simplemod.py` file in the WebIDE and modify the `Spam` class:

```python
# simplemod.py
# ... (leave the rest of the file unchanged)

class Spam:
    def yow(self):
        print('More Yow!')  # Changed from 'Yow!'
```

5. Save the file and return to the terminal. Start the Python interpreter and create a new instance:

```bash
python3
```

```python
>>> import simplemod
Loaded simplemod
>>> t = simplemod.Spam()
>>> t.yow()
More Yow!
```

6. Now let us demonstrate what happens with reloading:

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
```

7. Exit Python, modify the file again, and then test both instances:

```python
>>> exit()
```

8. Update the `simplemod.py` file:

```python
# simplemod.py
# ... (leave the rest of the file unchanged)

class Spam:
    def yow(self):
        print('Even More Yow!')  # Changed again
```

9. Save the file and return to the terminal:

```bash
python3
```

```python
>>> import simplemod
Loaded simplemod
>>> s = simplemod.Spam()
>>> s.yow()
Even More Yow!

>>> # Exit without closing Python, edit the file
```

10. Without closing Python, open `simplemod.py` in the WebIDE and change it:

```python
# simplemod.py
# ... (leave the rest of the file unchanged)

class Spam:
    def yow(self):
        print('Super Yow!')  # Changed one more time
```

11. Save the file and go back to the Python interpreter:

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>

>>> # Try the old instance
>>> s.yow()
Even More Yow!  # Still uses the old implementation

>>> # Create a new instance
>>> t = simplemod.Spam()
>>> t.yow()
Super Yow!  # Uses the new implementation
```

Notice that the old instance `s` still uses the old implementation, while the new instance `t` uses the new implementation. This happens because reloading a module does not update existing instances of classes.

12. You can also observe other unusual behaviors:

```python
>>> isinstance(s, simplemod.Spam)
False
>>> isinstance(t, simplemod.Spam)
True
```

This indicates that after reloading, `simplemod.Spam` refers to a different class object than the one used to create `s`.

These limitations make module reloading useful primarily for development and debugging, but not recommended for production code.
