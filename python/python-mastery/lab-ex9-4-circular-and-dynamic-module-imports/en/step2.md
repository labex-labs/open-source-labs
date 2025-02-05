# Circular Imports

Try moving the following import statements to the top of the `formatter.py` file:

```python
# formatter.py

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

...
```

Observe that nothing works anymore. Try running the `stock.py` program and notice the error about `TableFormatter` not being defined. The order of import statements matters and you can't just move the imports anywhere you want.

Move the import statements back where they were. Sigh.
