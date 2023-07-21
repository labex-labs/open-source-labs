# Application Structure

Code organization and file structure is key to the maintainability of
an application.

There is no "one-size fits all" approach for Python. However, one
structure that works for a lot of problems is something like this.

```code
porty-app/
  README.txt
  script.py         # SCRIPT
  porty/
    # LIBRARY CODE
    __init__.py
    pcost.py
    report.py
    fileparse.py
```

The top-level `porty-app` is a container for everything else--documentation,
top-level scripts, examples, etc.

Again, top-level scripts (if any) need to exist outside the code
package. One level up.

```python
#!/usr/bin/env python3
# porty-app/script.py
import sys
import porty

porty.report.main(sys.argv)
```

At this point, you have a directory with several programs:

```
pcost.py          # computes portfolio cost
report.py         # Makes a report
ticker.py         # Produce a real-time stock ticker
```

There are a variety of supporting modules with other functionality:

```
stock.py          # Stock class
portfolio.py      # Portfolio class
fileparse.py      # CSV parsing
tableformat.py    # Formatted tables
follow.py         # Follow a log file
typedproperty.py  # Typed class properties
```

In this exercise, we're going to clean up the code and put it into
a common package.
