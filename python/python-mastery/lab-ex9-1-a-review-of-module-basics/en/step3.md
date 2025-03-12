# Understanding Module Loading Behavior

In Python, the way modules are loaded has some interesting characteristics. In this step, we'll explore these behaviors to understand how Python manages module loading.

1. First, let's see what happens when we try to import a module again within the same Python interpreter session. When you start a Python interpreter, it's like opening a workspace where you can run Python code. Once you've imported a module, importing it again might seem like it would reload the module, but that's not the case.

```python
>>> import simplemod
```

Notice that this time you do not see the "Loaded simplemod" output. This is because **Python only loads a module once** per interpreter session. Subsequent `import` statements do not reload the module. Python remembers that it has already loaded the module, so it doesn't go through the process of loading it again.

2. After importing a module, you can modify the variables inside it. A module in Python is like a container that holds variables, functions, and classes. Once you've imported a module, you can access and change its variables just like you would with any other Python object.

```python
>>> simplemod.x
42
>>> simplemod.x = 13
>>> simplemod.x
13
>>> simplemod.foo()
x is 13
```

Here, we first check the value of the variable `x` in the `simplemod` module, which is initially `42`. Then we change its value to `13` and verify that the change has been made. When we call the `foo` function in the module, it reflects the new value of `x`.

3. Importing the module again does not reset the changes we made to its variables. Even if we try to import the module once more, Python doesn't reload it, so the changes we made to its variables remain.

```python
>>> import simplemod
>>> simplemod.x
13
```

4. If you want to forcibly reload a module, you need to use the `importlib.reload()` function. Sometimes, you might have made changes to the module's code and want to see those changes take effect immediately. The `importlib.reload()` function allows you to do just that.

```python
>>> import importlib
>>> importlib.reload(simplemod)
Loaded simplemod
<module 'simplemod' from 'simplemod.py'>
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
```

The module has been reloaded, and the value of `x` has been reset to `42`. This shows that the module has been loaded again from its source code, and all the variables have been initialized as they were originally.

5. Python keeps track of all loaded modules in the `sys.modules` dictionary. This dictionary acts as a registry where Python stores information about all the modules that have been loaded during the current interpreter session.

```python
>>> 'simplemod' in sys.modules
True
>>> sys.modules['simplemod']
<module 'simplemod' from 'simplemod.py'>
```

By checking if a module name is in the `sys.modules` dictionary, you can see if the module has been loaded. And by accessing the dictionary with the module name as the key, you can get information about the module.

6. You can remove a module from this dictionary to force Python to reload it on the next import. If you remove a module from the `sys.modules` dictionary, Python forgets that it has already loaded the module. So, the next time you try to import it, Python will load it again from its source code.

```python
>>> del sys.modules['simplemod']
>>> import simplemod
Loaded simplemod
>>> simplemod.x
42
```

The module was loaded again because it was removed from `sys.modules`. This is another way to ensure that you're working with the latest version of a module's code.
