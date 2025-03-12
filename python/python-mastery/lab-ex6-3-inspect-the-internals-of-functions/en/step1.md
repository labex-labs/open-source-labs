# Exploring Function Attributes

In Python, functions are considered first-class objects. What does this mean? Well, it's similar to how you have different types of objects in the real world, like a book or a pen. In Python, functions are also objects, and just like other objects, they come with their own set of attributes. These attributes can give us a lot of useful information about the function, such as its name, where it's defined, and how it's implemented.

Let's start our exploration by opening a Python interactive shell. This shell is like a playground where we can write and run Python code right away. To do this, we'll first navigate to the project directory and then start the Python interpreter. Here are the commands to run in your terminal:

```bash
cd ~/project
python3
```

Now that we're in the Python interactive shell, let's define a simple function. This function will take two numbers and add them together. Here's how we can define it:

```python
def add(x, y):
    'Adds two things'
    return x + y
```

In this code, we've created a function named `add`. It takes two parameters, `x` and `y`, and returns their sum. The string `'Adds two things'` is called a docstring, which is used to document what the function does.

## Using dir() to Inspect Function Attributes

In Python, the `dir()` function is a handy tool. It can be used to get a list of all the attributes and methods that an object has. Let's use it to see what attributes our `add` function has. Run the following code in the Python interactive shell:

```python
dir(add)
```

When you run this code, you'll see a long list of attributes. Here's an example of what the output might look like:

```
['__annotations__', '__call__', '__class__', '__closure__', '__code__', '__defaults__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__get__', '__getattribute__', '__globals__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__kwdefaults__', '__le__', '__lt__', '__module__', '__name__', '__ne__', '__new__', '__qualname__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__']
```

This list shows all the attributes and methods associated with the `add` function.

## Accessing Basic Function Information

Now, let's take a closer look at some of the basic function attributes. These attributes can tell us important information about the function. Run the following code in the Python interactive shell:

```python
print(add.__name__)
print(add.__module__)
print(add.__doc__)
```

When you run this code, you'll see the following output:

```
add
__main__
Adds two things
```

Let's understand what each of these attributes means:

- `__name__`: This attribute gives us the name of the function. In our case, the function is named `add`.
- `__module__`: It tells us the module where the function is defined. When we run code in the interactive shell, the module is usually `__main__`.
- `__doc__`: This is the function's documentation string, or docstring. It provides a brief description of what the function does.

## Examining Function Code

The `__code__` attribute of a function is very interesting. It contains information about how the function is implemented, including its bytecode and other details. Let's see what we can learn from it. Run the following code in the Python interactive shell:

```python
print(add.__code__.co_varnames)
print(add.__code__.co_argcount)
```

The output will be:

```
('x', 'y')
2
```

Here's what these attributes tell us:

- `co_varnames`: It's a tuple that contains the names of all the local variables used by the function. In our `add` function, the local variables are `x` and `y`.
- `co_argcount`: This attribute tells us the number of arguments that the function expects. Our `add` function expects two arguments, so the value is 2.

If you're curious to explore more attributes of the `__code__` object, you can use the `dir()` function again. Run the following code:

```python
dir(add.__code__)
```

This will display all the attributes of the code object, which contain low-level details about how the function is implemented.
