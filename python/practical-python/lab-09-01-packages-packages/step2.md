# Packages vs Modules

For larger collections of code, it is common to organize modules into
a package.

```code
# From this
pcost.py
report.py
fileparse.py

# To this
porty/
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

You pick a name and make a top-level directory. `porty` in the example
above (clearly picking this name is the most important first step).

Add an `__init__.py` file to the directory. It may be empty.

Put your source files into the directory.
