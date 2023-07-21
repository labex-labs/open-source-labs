# Standard Library Modules

Modules from Python's standard library usually come from a location
such as `/usr/local/lib/python3.6'. You can find out for certain
by trying a short test:

```python
>>> import re
>>> re
<module 're' from '/usr/local/lib/python3.6/re.py'>
>>>
```

Simply looking at a module in the REPL is a good debugging tip
to know about. It will show you the location of the file.
