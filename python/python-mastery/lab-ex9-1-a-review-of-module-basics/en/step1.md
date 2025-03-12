# Creating a Simple Module

Let's begin our journey into Python modules by creating a simple one. In Python, a module is essentially a file with a `.py` extension that holds Python code. Think of it as a container where you can group related functions, classes, and variables together. This makes your code more organized and easier to manage, especially as your projects grow in size.

1. First, open the WebIDE. Once it's open, you'll need to create a new file. To do this, click on "File" in the menu bar, and then select "New File". Name this new file `simplemod.py` and save it in the `/home/labex/project` directory. This directory is where we'll keep all the files related to this experiment.

2. Now, let's add some code to our newly created `simplemod.py` file. The code below defines a few basic elements that you'll commonly find in a Python module.

```python
# simplemod.py

x = 42        # A global variable

# A simple function
def foo():
    print('x is', x)

# A simple class
class Spam:
    def yow(self):
        print('Yow!')

# A scripting statement
print('Loaded simplemod')
```

In this code:

- `x = 42` creates a global variable named `x` and assigns it the value `42`. Global variables can be accessed from anywhere within the module.
- The `foo()` function is defined to print the value of the global variable `x`. Functions are reusable blocks of code that perform a specific task.
- The `Spam` class is a blueprint for creating objects. It has a method called `yow()`, which simply prints the string 'Yow!'. Methods are functions that belong to a class.
- The `print('Loaded simplemod')` statement is a scripting statement. It will execute as soon as the module is loaded, which helps us confirm that the module has been successfully loaded.

3. After adding the code, save the file. You can do this by pressing `Ctrl+S` on your keyboard or by selecting "File" > "Save" from the menu. Saving the file ensures that all the changes you've made are preserved.

Let's take a closer look at what this module contains:

- A global variable `x` with the value `42`. This variable can be used throughout the module and even accessed from other modules if imported correctly.
- A function `foo()` that prints the value of `x`. Functions are useful for performing repetitive tasks without having to write the same code multiple times.
- A class `Spam` with a method `yow()`. Classes and methods are fundamental concepts in object - oriented programming, which allows you to create complex data structures and behaviors.
- A `print` statement that executes when the module is loaded. This statement serves as a visual indicator that the module has been successfully loaded into the Python environment.

The `print` statement at the bottom will help us observe when the module is loaded, which is important for debugging and understanding how modules work in Python.
