# The Module Search Path

`sys.path` is a directory that contains the list of all directories
checked by the `import` statement. Look at it:

```python
>>> import sys
>>> sys.path
... look at the result ...
>>>
```

If you import something and it's not located in one of those
directories, you will get an `ImportError` exception.
