# Argument Passing

When you call a function, the argument variables are names that refer
to the passed values. These values are NOT copies (see [section
2.7](../02_Working_with_data/07_Objects.md)). If mutable data types are
passed (e.g. lists, dicts), they can be modified _in-place_.

```python
def foo(items):
    items.append(42)    # Modifies the input object

a = [1, 2, 3]
foo(a)
print(a)                # [1, 2, 3, 42]
```

**Key point: Functions don't receive a copy of the input arguments.**
