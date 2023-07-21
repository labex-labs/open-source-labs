# Exercise 9.1: Making a simple package

Make a directory called `porty/` and put all of the above Python
files into it. Additionally create an empty `__init__.py` file and
put it in the directory. You should have a directory of files
like this:

```
porty/
    __init__.py
    fileparse.py
    follow.py
    pcost.py
    portfolio.py
    report.py
    stock.py
    tableformat.py
    ticker.py
    typedproperty.py
```

Remove the file `__pycache__` that's sitting in your directory. This
contains pre-compiled Python modules from before. We want to start
fresh.

Try importing some of package modules:

```python
>>> import porty.report
>>> import porty.pcost
>>> import porty.ticker
```

If these imports fail, go into the appropriate file and fix the
module imports to include a package-relative import. For example,
a statement such as `import fileparse` might change to the
following:

```
# report.py
from . import fileparse
...
```

If you have a statement such as `from fileparse import parse_csv`, change
the code to the following:

```
# report.py
from .fileparse import parse_csv
...
```
