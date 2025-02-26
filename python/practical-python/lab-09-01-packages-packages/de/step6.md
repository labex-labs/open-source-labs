# Relative Imports

Anstatt direkt den Paketnamen zu verwenden, können Sie `.` verwenden, um auf das aktuelle Paket zu verweisen.

```python
from. import fileparse

def read_portfolio(filename):
    return fileparse.parse_csv(...)
```

Syntax:

```python
from. import modname
```

Dies macht es einfach, das Paket umzubenennen.
