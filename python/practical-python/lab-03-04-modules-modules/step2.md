# Namespaces

A module is a collection of named values and is sometimes said to be a
_namespace_. The names are all of the global variables and functions
defined in the source file. After importing, the module name is used
as a prefix. Hence the _namespace_.

```python
import foo

a = foo.grok(2)
b = foo.spam('Hello')
...
```

The module name is directly tied to the file name (foo -> foo.py).
