# Importing and Using Modules

Now that we have created a module, let us import it and use its components.

1. Open a new terminal in the WebIDE by clicking on "Terminal" > "New Terminal".

2. Start the Python interpreter by typing:

```bash
python3
```

3. Import the module using the `import` statement:

```python
>>> import simplemod
Loaded simplemod
```

Notice that you see "Loaded simplemod" in the output. This is because the `print` statement in our module executes when the module is loaded.

4. Now that you have imported the module, you can access its components using dot notation:

```python
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
>>> spam_instance = simplemod.Spam()
>>> spam_instance.yow()
Yow!
```

5. If you encounter an `ImportError` when importing the module, it means Python cannot find your module. Check the directories Python searches for modules by examining `sys.path`:

```python
>>> import sys
>>> sys.path
['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
```

Your current working directory (the first empty string in the list) should be included in the path. This is where Python looks for the `simplemod.py` file.
