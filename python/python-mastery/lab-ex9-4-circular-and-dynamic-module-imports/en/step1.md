# Understanding the Import Problem

Let's begin by examining an example of a problematic module structure. The code in `tableformat/formatter.py` has imports scattered throughout the file, which creates maintenance and dependency issues.

Open the WebIDE file explorer and navigate to the `structly` directory. Let's examine the current structure of the project by running:

```bash
cd ~/project/structly
ls -la
```

This will show you the files in the project directory. Now let's look at one of the problematic files:

```bash
cat tableformat/formatter.py
```

You should see code similar to:

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

def create_formatter(name, column_formats=None, upper_headers=False):
    if name == 'text':
        formatter_cls = TextTableFormatter
    elif name == 'csv':
        formatter_cls = CSVTableFormatter
    elif name == 'html':
        formatter_cls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter_cls(ColumnFormatMixin, formatter_cls):
              formats = column_formats

    if upper_headers:
        class formatter_cls(UpperHeadersMixin, formatter_cls):
            pass

    return formatter_cls()
```

Notice the placement of import statements in the middle of the file. This is problematic because:

1. It makes the code harder to read and maintain
2. It can lead to circular import issues
3. It breaks the Python convention of placing all imports at the top of a file

In the following steps, we'll explore these issues and learn how to resolve them.
