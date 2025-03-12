# Understanding the Import Problem

Let's start by understanding what module imports are. In Python, when you want to use functions, classes, or variables from another file (module), you use the `import` statement. However, the way you structure your imports can lead to various issues.

Now, we're going to examine an example of a problematic module structure. The code in `tableformat/formatter.py` has imports scattered throughout the file. This might not seem like a big deal at first, but it creates maintenance and dependency issues.

First, open the WebIDE file explorer and navigate to the `structly` directory. We'll run a couple of commands to understand the current structure of the project. The `cd` command is used to change the current working directory, and the `ls -la` command lists all the files and directories in the current directory, including hidden ones.

```bash
cd ~/project/structly
ls -la
```

This will show you the files in the project directory. Now, we'll look at one of the problematic files using the `cat` command, which displays the contents of a file.

```bash
cat tableformat/formatter.py
```

You should see code similar to the following:

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

Notice the placement of import statements in the middle of the file. This is problematic for several reasons:

1. It makes the code harder to read and maintain. When you're looking at a file, you expect to see all the imports at the beginning so you can quickly understand what external modules the file depends on.
2. It can lead to circular import issues. Circular imports happen when two or more modules depend on each other, which can cause errors and make your code behave unexpectedly.
3. It breaks the Python convention of placing all imports at the top of a file. Following conventions makes your code more readable and easier for other developers to understand.

In the following steps, we'll explore these issues in more detail and learn how to resolve them.
