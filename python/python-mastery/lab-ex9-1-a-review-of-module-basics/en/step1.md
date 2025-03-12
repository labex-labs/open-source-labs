# Creating a Simple Module

Let us start by creating a simple Python module. A module in Python is simply a file with a `.py` extension containing Python code.

1. Open the WebIDE and create a new file called `simplemod.py` in the `/home/labex/project` directory by clicking on "File" > "New File".

2. Add the following code to the file:

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

3. Save the file by pressing `Ctrl+S` or selecting "File" > "Save".

Let us examine what this module contains:

- A global variable `x` with the value `42`
- A function `foo()` that prints the value of `x`
- A class `Spam` with a method `yow()`
- A `print` statement that executes when the module is loaded

The `print` statement at the bottom will help us observe when the module is loaded.
