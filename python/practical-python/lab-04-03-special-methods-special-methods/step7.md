# Attribute Access

There is an alternative way to access, manipulate and manage attributes.

```python
getattr(obj, 'name')          # Same as obj.name
setattr(obj, 'name', value)   # Same as obj.name = value
delattr(obj, 'name')          # Same as del obj.name
hasattr(obj, 'name')          # Tests if attribute exists
```

Example:

```python
if hasattr(obj, 'x'):
    x = getattr(obj, 'x'):
else:
    x = None
```

*Note: `getattr()` also has a useful default value *arg\*.

```python
x = getattr(obj, 'x', None)
```
