# Importing and Using Modules

Now that we have created a module, it's time to understand how to import it and use its components. In Python, a module is a file containing Python definitions and statements. When you import a module, you gain access to all the functions, classes, and variables defined within it. This allows you to reuse code and organize your programs more effectively.

1. First, we need to open a new terminal in the WebIDE. This terminal will serve as our workspace where we can run Python commands. To open a new terminal, click on "Terminal" > "New Terminal".

2. Once the terminal is open, we need to start the Python interpreter. The Python interpreter is a program that reads and executes Python code. To start it, type the following command in the terminal and press Enter:

```bash
python3
```

3. Now that the Python interpreter is running, we can import our module. In Python, we use the `import` statement to bring a module into our current program. Type the following command in the Python interpreter:

```python
>>> import simplemod
Loaded simplemod
```

You'll notice that "Loaded simplemod" appears in the output. This is because the `print` statement in our `simplemod` module executes when the module is loaded. When Python imports a module, it runs all the top - level code in that module, including any `print` statements.

4. After importing the module, we can access its components using dot notation. Dot notation is a way to access attributes (variables and functions) of an object in Python. In this case, the module is an object, and its functions, variables, and classes are its attributes. Here are some examples of how to access different components of the `simplemod` module:

```python
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
>>> spam_instance = simplemod.Spam()
>>> spam_instance.yow()
Yow!
```

In the first line, we access the variable `x` defined in the `simplemod` module. In the second line, we call the function `foo` from the `simplemod` module. In the third and fourth lines, we create an instance of the `Spam` class defined in the `simplemod` module and call its method `yow`.

5. Sometimes, you might encounter an `ImportError` when trying to import a module. This error occurs when Python cannot find the module you are trying to import. To figure out where Python is looking for modules, you can examine the `sys.path` variable. The `sys.path` variable is a list of directories that Python searches when looking for modules. Type the following commands in the Python interpreter:

```python
>>> import sys
>>> sys.path
['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
```

The first element in the list (the empty string) represents the current working directory. This is where Python looks for the `simplemod.py` file. If your module is not in one of the directories listed in `sys.path`, Python won't be able to find it, and you'll get an `ImportError`. Make sure your `simplemod.py` file is in the current working directory or one of the other directories in `sys.path`.