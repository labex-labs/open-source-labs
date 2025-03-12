# Using the inspect Module

In Python, the standard library comes with a very useful `inspect` module. This module is like a detective tool that helps us gather information about live objects in Python. Live objects can be things like modules, classes, and functions. Instead of manually digging through an object's attributes to find information, the `inspect` module provides more organized and high - level ways to understand the properties of functions.

Let's keep using the same Python interactive shell to explore how this module works.

## Function Signatures

The `inspect.signature()` function is a handy tool. When you pass a function to it, it returns a `Signature` object. This object holds important details about the function's parameters.

Here's an example. Suppose we have a function named `add`. We can use the `inspect.signature()` function to get its signature:

```python
import inspect
sig = inspect.signature(add)
print(sig)
```

When you run this code, the output will be:

```
(x, y)
```

This output shows us the function's signature, which tells us what parameters the function can accept.

## Examining Parameter Details

We can go a step further and get more in - depth information about each parameter of the function.

```python
print(sig.parameters)
```

The output of this code will be:

```
OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)])
```

The parameters of the function are stored in an ordered dictionary. Sometimes, we might only be interested in the names of the parameters. We can convert this ordered dictionary to a tuple to extract just the parameter names.

```python
param_names = tuple(sig.parameters)
print(param_names)
```

The output will be:

```
('x', 'y')
```

## Examining Individual Parameters

We can also take a closer look at each individual parameter. The following code loops through each parameter in the function and prints out some important details about it.

```python
for name, param in sig.parameters.items():
    print(f"Parameter: {name}")
    print(f"  Kind: {param.kind}")
    print(f"  Default: {param.default if param.default is not param.empty else 'No default'}")
```

This code will show us details about each parameter. It tells us the kind of the parameter (whether it's a positional parameter, a keyword parameter, etc.) and its default value if it has one.

The `inspect` module has many other useful functions for function introspection. Here are some examples:

- `inspect.getdoc(obj)`: This function retrieves the documentation string for an object. Documentation strings are like notes that programmers write to explain what an object does.
- `inspect.getfile(obj)`: It helps us find out the file where an object is defined. This can be very useful when we want to locate the source code of an object.
- `inspect.getsource(obj)`: This function fetches the source code of an object. It allows us to see exactly how the object is implemented.
