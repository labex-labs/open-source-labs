# Using the inspect Module

Python's standard library includes a powerful `inspect` module that provides functions to get information about live objects such as modules, classes, functions, and more. This module offers more structured and higher-level ways to inspect function properties than manually accessing attributes.

Let's continue using the same Python interactive shell:

## Function Signatures

The `inspect.signature()` function returns a Signature object that contains information about the function's parameters:

```python
import inspect
sig = inspect.signature(add)
print(sig)
```

Output:

```
(x, y)
```

This gives us the function's signature, which shows the parameters it accepts.

## Examining Parameter Details

We can get more information about each parameter:

```python
print(sig.parameters)
```

Output:

```
OrderedDict([('x', <Parameter "x">), ('y', <Parameter "y">)])
```

The parameters are stored in an ordered dictionary, which we can convert to a tuple to get just the parameter names:

```python
param_names = tuple(sig.parameters)
print(param_names)
```

Output:

```
('x', 'y')
```

## Examining Individual Parameters

We can also examine individual parameters more closely:

```python
for name, param in sig.parameters.items():
    print(f"Parameter: {name}")
    print(f"  Kind: {param.kind}")
    print(f"  Default: {param.default if param.default is not param.empty else 'No default'}")
```

This would show details about each parameter, including its kind (positional, keyword, etc.) and default value if any.

The inspect module offers many other useful functions for function introspection, such as:

- `inspect.getdoc(obj)`: Get the documentation string for an object
- `inspect.getfile(obj)`: Get the file where an object is defined
- `inspect.getsource(obj)`: Get the source code of an object
