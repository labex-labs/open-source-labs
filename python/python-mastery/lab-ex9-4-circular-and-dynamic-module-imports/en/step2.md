# Exploring Circular Imports

A circular import is a situation where two or more modules depend on each other. Specifically, when module A imports module B, and module B also imports module A, either directly or indirectly. This creates a dependency loop that Python's import system cannot resolve properly. In simpler terms, Python gets stuck in a loop trying to figure out which module to import first, and this can lead to errors in your program.

Let's experiment with our code to see how circular imports can cause problems.

First, we'll run the stock program to check if it works with the current structure. This step helps us establish a baseline and see the program working as expected before we make any changes.

```bash
cd ~/project/structly
python3 stock.py
```

The program should run correctly and display stock data in a formatted table. If it does, that means the current code structure is working fine without any circular import issues.

Now, we're going to modify the `formatter.py` file. Usually, it's a good practice to move imports to the top of a file. This makes the code more organized and easier to understand at a glance.

```bash
cd ~/project/structly
```

Open `tableformat/formatter.py` in the WebIDE. We'll move the following imports to the top of the file, right after the existing imports. These imports are for different table formatters, like text, CSV, and HTML.

```python
from .formats.text import TextTableFormatter
from .formats.csv import CSVTableFormatter
from .formats.html import HTMLTableFormatter
```

So the beginning of the file should now look like this:

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

Save the file and try running the stock program again.

```bash
python3 stock.py
```

You should see an error message about `TableFormatter` not being defined. This is a clear sign of a circular import problem.

The issue occurs because of the following chain of events:

1. `formatter.py` tries to import `TextTableFormatter` from `formats/text.py`.
2. `formats/text.py` imports `TableFormatter` from `formatter.py`.
3. When Python tries to resolve these imports, it gets stuck in a loop because it can't decide which module to fully import first.

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

Run the program again to confirm it's working.

```bash
python3 stock.py
```

This demonstrates that even though having imports in the middle of the file is not the best practice in terms of code organization, it was done to avoid a circular import problem. In the next steps, we'll explore better solutions.
