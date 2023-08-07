# `__main__` check

It is standard practice for modules that run as a main script to use this convention:

```python
# prog.py
...
if __name__ == '__main__':
    # Running as the main program ...
    statements
    ...
```

Statements enclosed inside the `if` statement become the _main_ program.
