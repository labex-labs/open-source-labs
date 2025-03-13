# Exploring Module Reloading Limitations

Module reloading is a useful feature in Python, but it comes with some limitations, especially when dealing with classes. In this section, we'll explore these limitations step by step. Understanding these limitations is crucial for both development and production environments.

1. Restart the Python interpreter:
   First, we need to restart the Python interpreter. This step is important because it ensures that we start with a clean slate. When you restart the interpreter, all previously imported modules and variables are cleared. To exit the current Python interpreter, use the `exit()` command. Then, start a new Python interpreter session using the `python3` command in the terminal.

```python
>>> exit()
```

```bash
python3
```

2. Import the module and create an instance of the `Spam` class:
   Now that we have a fresh Python interpreter session, we'll import the `simplemod` module. Importing a module allows us to use the classes, functions, and variables defined in that module. After importing the module, we'll create an instance of the `Spam` class and call its `yow()` method. This will help us see the initial behavior of the class.

```python
>>> import simplemod
Loaded simplemod
>>> s = simplemod.Spam()
>>> s.yow()
Yow!
```

3. Now let us modify the `Spam` class in our module. Exit the Python interpreter:
   Next, we're going to make changes to the `Spam` class in the `simplemod` module. Before we do that, we need to exit the Python interpreter. This is because we want to make changes to the source code of the module and then see how those changes affect the behavior of the class.

```python
>>> exit()
```

4. Open the `simplemod.py` file in the WebIDE and modify the `Spam` class:
   Open the `simplemod.py` file in the WebIDE. This is where the source code of the `simplemod` module is located. We'll modify the `yow()` method of the `Spam` class to print a different message. This change will help us observe how the behavior of the class changes after reloading the module.

```python
# simplemod.py
# ... (leave the rest of the file unchanged)

class Spam:
    def yow(self):
        print('More Yow!')  # Changed from 'Yow!'
```

5. Save the file and return to the terminal. Start the Python interpreter and create a new instance:
   After making the changes to the `simplemod.py` file, save it. Then, return to the terminal and start a new Python interpreter session. Import the `simplemod` module again and create a new instance of the `Spam` class. Call the `yow()` method of the new instance to see the updated behavior.

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
   To see how module reloading works, we'll use the `importlib.reload()` function. This function allows us to reload a previously imported module. After reloading the module, we'll see if the changes we made to the `Spam` class are reflected.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
```

7. Exit Python, modify the file again, and then test both instances:
   Exit the Python interpreter once more. Then, make another change to the `Spam` class in the `simplemod.py` file. After that, we'll test both the old and new instances of the `Spam` class to see how they behave.

```python
>>> exit()
```

8. Update the `simplemod.py` file:
   Open the `simplemod.py` file again and modify the `yow()` method of the `Spam` class to print a different message. This change will help us further understand the limitations of module reloading.

```python
# simplemod.py
# ... (leave the rest of the file unchanged)

class Spam:
    def yow(self):
        print('Even More Yow!')  # Changed again
```

9. Save the file and return to the terminal:
   Save the changes to the `simplemod.py` file and return to the terminal. Start a new Python interpreter session, import the `simplemod` module, and create a new instance of the `Spam` class. Call the `yow()` method of the new instance to see the updated behavior.

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
    Without closing the Python interpreter, open the `simplemod.py` file in the WebIDE and make another change to the `yow()` method of the `Spam` class. This will help us see how the behavior of existing and new instances changes after reloading the module.

```python
# simplemod.py
# ... (leave the rest of the file unchanged)

class Spam:
    def yow(self):
        print('Super Yow!')  # Changed one more time
```

11. Save the file and go back to the Python interpreter:
    Save the changes to the `simplemod.py` file and go back to the Python interpreter. Reload the `simplemod` module using the `importlib.reload()` function. Then, test both the old and new instances of the `Spam` class to see how they behave.

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

Notice that the old instance `s` still uses the old implementation, while the new instance `t` uses the new implementation. This happens because reloading a module does not update existing instances of classes. When a class instance is created, it stores a reference to the class object at that time. Reloading the module creates a new class object, but the existing instances still refer to the old class object.

12. You can also observe other unusual behaviors:
    We can further observe the limitations of module reloading by using the `isinstance()` function. This function checks if an object is an instance of a particular class. After reloading the module, we'll see that the old instance `s` is no longer considered an instance of the new `simplemod.Spam` class, while the new instance `t` is.

```python
>>> isinstance(s, simplemod.Spam)
False
>>> isinstance(t, simplemod.Spam)
True
```

This indicates that after reloading, `simplemod.Spam` refers to a different class object than the one used to create `s`.

These limitations make module reloading useful primarily for development and debugging, but not recommended for production code. In a production environment, it's important to ensure that all instances of a class use the same, up - to - date implementation. Module reloading can lead to inconsistent behavior, which can be difficult to debug and maintain.