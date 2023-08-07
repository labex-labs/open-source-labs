# Module Loading

Each module loads and executes only _once_. _Note: Repeated imports just return a reference to the previously loaded module._

`sys.modules` is a dict of all loaded modules.

```python
>>> import sys
>>> sys.modules.keys()
['copy_reg', '__main__', 'site', '__builtin__', 'encodings', 'encodings.encodings', 'posixpath', ...]
>>>
```

**Caution:** A common confusion arises if you repeat an `import` statement after changing the source code for a module. Because of the module cache `sys.modules`, repeated imports always return the previously loaded module--even if a change was made. The safest way to load modified code into Python is to quit and restart the interpreter.
