# Exploring Circular Imports

A circular import occurs when module A imports module B, and module B also imports module A, either directly or indirectly. This creates a dependency loop that Python's import system cannot resolve properly.

Let's experiment with our code to see how circular imports can cause problems.

First, let's run the stock program to see if it works with the current structure:

```bash
cd ~/project/structly
python3 stock.py
```

The program should run correctly and display stock data in a formatted table.

Now, let's modify the `formatter.py` file to move the imports to the top, which would normally be good practice:

```bash
cd ~/project/structly
```

Open `tableformat/formatter.py` in the WebIDE and move the following imports to the top of the file, right after the existing imports:

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

So the beginning of the file should now look like:

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin
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
```

Save the file and try running the stock program again:

```bash
python3 stock.py
```

You should see an error message about `TableFormatter` not being defined. This is a circular import problem!

The issue occurs because:

1. `formatter.py` tries to import `TextTableFormatter` from `formats/text.py`
2. `formats/text.py` imports `TableFormatter` from `formatter.py`
3. When Python tries to resolve this, it gets stuck in a loop

Let's revert our changes to make the program work again. Edit `tableformat/formatter.py` and move the imports back to where they were originally (after the `TableFormatter` class definition).

```python
# formatter.py
from abc import ABC, abstractmethod
from .mixins import ColumnFormatMixin, UpperHeadersMixin

class TableFormatter(ABC):
    @abstractmethod
    def headings(self, headers):
        pass

    @abstractmethod
    def row(self, rowdata):
        pass

from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

Run the program again to confirm it's working:

```bash
python3 stock.py
```

This demonstrates that even though having imports in the middle of the file is not ideal, it was done to avoid a circular import problem. In the next steps, we'll explore better solutions.
