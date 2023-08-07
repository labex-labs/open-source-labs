# Type Checking

How to tell if an object is a specific type.

```python
if isinstance(a, list):
    print('a is a list')
```

Checking for one of many possible types.

```python
if isinstance(a, (list,tuple)):
    print('a is a list or tuple')
```

\*Caution: Don't go overboard with type checking. It can lead to excessive code complexity. Usually you'd only do it if doing so would prevent common mistakes made by others using your code.

-
