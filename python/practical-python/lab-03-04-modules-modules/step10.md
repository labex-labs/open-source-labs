# Locating Modules

Python consults a path list (sys.path) when looking for modules.

```python
>>> import sys
>>> sys.path
[
  '',
  '/usr/local/lib/python36/python36.zip',
  '/usr/local/lib/python36',
  ...
]
```

The current working directory is usually first.
