# 模块拆分以实现更好的代码组织

随着你的 Python 项目不断发展，你可能会发现单个模块文件变得非常大，并且包含多个相关但不同的组件。当这种情况发生时，将模块拆分为包含子模块的包是一种很好的做法。这种方法可以让你的代码更有条理、更易于维护，并且更具可扩展性。

## 了解当前结构

`tableformat.py` 模块是一个大型模块的典型例子。它包含几个格式化器类，每个类负责以不同的方式格式化数据：

- `TableFormatter`（基类）：这是所有其他格式化器类的基类。它定义了其他类将继承和实现的基本结构和方法。
- `TextTableFormatter`：这个类以纯文本格式格式化数据。
- `CSVTableFormatter`：这个类以 CSV（逗号分隔值）格式格式化数据。
- `HTMLTableFormatter`：这个类以 HTML（超文本标记语言）格式格式化数据。

我们将把这个模块重新组织成一个包结构，为每种格式化器类型创建单独的文件。这将使代码更具模块化，更易于管理。

## 步骤 1：清理缓存文件

在开始重新组织代码之前，清理所有 Python 缓存文件是个不错的主意。这些文件是 Python 为加速代码执行而创建的，但在你对代码进行更改时，它们有时会导致问题。

```bash
cd ~/project/structly
rm -rf __pycache__
```

在上述命令中，`cd ~/project/structly` 将当前目录更改为你项目中的 `structly` 目录。`rm -rf __pycache__` 删除 `__pycache__` 目录及其所有内容。`-r` 选项表示递归，这意味着它将删除 `__pycache__` 目录内的所有文件和子目录。`-f` 选项表示强制，这意味着它将在不要求确认的情况下删除文件。

## 步骤 2：创建新的包结构

现在，让我们为我们的包创建一个新的目录结构。我们将创建一个名为 `tableformat` 的目录，并在其中创建一个名为 `formats` 的子目录。

```bash
mkdir -p tableformat/formats
```

`mkdir` 命令用于创建目录。`-p` 选项表示父目录，如果必要的父目录不存在，它将创建所有必要的父目录。因此，如果 `tableformat` 目录不存在，它将首先被创建，然后在其中创建 `formats` 目录。

## 步骤 3：移动并重命名原始文件

接下来，我们将把原始的 `tableformat.py` 文件移动到新结构中，并将其重命名为 `formatter.py`。

```bash
mv tableformat.py tableformat/formatter.py
```

`mv` 命令用于移动或重命名文件。在这种情况下，我们将 `tableformat.py` 文件移动到 `tableformat` 目录并将其重命名为 `formatter.py`。

## 步骤 4：将代码拆分为单独的文件

现在我们需要为每个格式化器创建文件，并将相关代码移动到这些文件中。

### 1. 创建基础格式化器文件

```bash
touch tableformat/formatter.py
```

`touch` 命令用于创建一个空文件。在这种情况下，我们在 `tableformat` 目录中创建一个名为 `formatter.py` 的文件。

我们将把 `TableFormatter` 基类以及任何通用实用函数（如 `print_table` 和 `create_formatter`）保留在这个文件中。该文件应该类似于以下内容：

```python
# Base TableFormatter class and utility functions

__all__ = ['TableFormatter', 'print_table', 'create_formatter']

class TableFormatter:
    def headings(self, headers):
        '''
        Emit table headings.
        '''
        raise NotImplementedError()

    def row(self, rowdata):
        '''
        Emit a single row of table data.
        '''
        raise NotImplementedError()

def print_table(objects, columns, formatter):
    '''
    Make a nicely formatted table from a list of objects and attribute names.
    '''
    formatter.headings(columns)
    for obj in objects:
        rowdata = [getattr(obj, name) for name in columns]
        formatter.row(rowdata)

def create_formatter(fmt):
    '''
    Create an appropriate formatter given an output format name.
    '''
    if fmt == 'text':
        from .formats.text import TextTableFormatter
        return TextTableFormatter()
    elif fmt == 'csv':
        from .formats.csv import CSVTableFormatter
        return CSVTableFormatter()
    elif fmt == 'html':
        from .formats.html import HTMLTableFormatter
        return HTMLTableFormatter()
    else:
        raise ValueError(f'Unknown format {fmt}')
```

`__all__` 变量用于指定当你使用 `from module import *` 时应该导入哪些符号。在这种情况下，我们指定只应导入 `TableFormatter`、`print_table` 和 `create_formatter` 符号。

`TableFormatter` 类是所有其他格式化器类的基类。它定义了两个方法 `headings` 和 `row`，这些方法应由子类实现。

`print_table` 函数是一个实用函数，它接受一个对象列表、一个列名列表和一个格式化器对象，并以格式化表格的形式打印数据。

`create_formatter` 函数是一个工厂函数，它接受一个格式名称作为参数，并返回一个合适的格式化器对象。

进行这些更改后，保存并退出文件。

### 2. 创建文本格式化器

```bash
touch tableformat/formats/text.py
```

我们将只把 `TextTableFormatter` 类添加到这个文件中。

```python
# Text formatter implementation

__all__ = ['TextTableFormatter']

from ..formatter import TableFormatter

class TextTableFormatter(TableFormatter):
    '''
    Emit a table in plain-text format
    '''
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))
```

`__all__` 变量指定当你使用 `from module import *` 时只应导入 `TextTableFormatter` 符号。

`from ..formatter import TableFormatter` 语句从父目录的 `formatter.py` 文件中导入 `TableFormatter` 类。

`TextTableFormatter` 类继承自 `TableFormatter` 类，并实现了 `headings` 和 `row` 方法，以纯文本格式格式化数据。

进行这些更改后，保存并退出文件。

### 3. 创建 CSV 格式化器

```bash
touch tableformat/formats/csv.py
```

我们将只把 `CSVTableFormatter` 类添加到这个文件中。

```python
# CSV formatter implementation

__all__ = ['CSVTableFormatter']

from ..formatter import TableFormatter

class CSVTableFormatter(TableFormatter):
    '''
    Output data in CSV format.
    '''
    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
```

与前面的步骤类似，我们指定 `__all__` 变量，导入 `TableFormatter` 类，并实现 `headings` 和 `row` 方法，以 CSV 格式格式化数据。

进行这些更改后，保存并退出文件。

### 4. 创建 HTML 格式化器

```bash
touch tableformat/formats/html.py
```

我们将只把 `HTMLTableFormatter` 类添加到这个文件中。

```python
# HTML formatter implementation

__all__ = ['HTMLTableFormatter']

from ..formatter import TableFormatter

class HTMLTableFormatter(TableFormatter):
    '''
    Output data in HTML format.
    '''
    def headings(self, headers):
        print('<tr>', end='')
        for h in headers:
            print(f'<th>{h}</th>', end='')
        print('</tr>')

    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print(f'<td>{d}</td>', end='')
        print('</tr>')
```

同样，我们指定 `__all__` 变量，导入 `TableFormatter` 类，并实现 `headings` 和 `row` 方法，以 HTML 格式格式化数据。

进行这些更改后，保存并退出文件。

## 步骤 5：创建包初始化文件

在 Python 中，`__init__.py` 文件用于将目录标记为 Python 包。我们需要在 `tableformat` 和 `formats` 目录中都创建 `__init__.py` 文件。

### 1. 为 `tableformat` 包创建一个文件

```bash
touch tableformat/__init__.py
```

将以下内容添加到文件中：

```python
# Re-export the original symbols from tableformat.py
from .formatter import *
```

此语句从 `formatter.py` 文件中导入所有符号，并在你导入 `tableformat` 包时使这些符号可用。

进行这些更改后，保存并退出文件。

### 2. 为 `formats` 包创建一个文件

```bash
touch tableformat/formats/__init__.py
```

你可以将此文件留空，或者添加一个简单的文档字符串：

```python
'''
Format implementations for different output formats.
'''
```

文档字符串简要描述了 `formats` 包的作用。

进行这些更改后，保存并退出文件。

## 步骤 6：测试新结构

让我们创建一个简单的测试，以验证我们的更改是否正确。

```bash
cd ~/project
touch test_tableformat.py
```

将以下内容添加到 `test_tableformat.py` 文件中：

```python
# Test the tableformat package restructuring

from structly import *

# Create formatters of each type
text_fmt = create_formatter('text')
csv_fmt = create_formatter('csv')
html_fmt = create_formatter('html')

# Define some test data
class TestData:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Create a list of test objects
data = [
    TestData('apple', 10),
    TestData('banana', 20),
    TestData('cherry', 30)
]

# Test text formatter
print("\nText Format:")
print_table(data, ['name', 'value'], text_fmt)

# Test CSV formatter
print("\nCSV Format:")
print_table(data, ['name', 'value'], csv_fmt)

# Test HTML formatter
print("\nHTML Format:")
print_table(data, ['name', 'value'], html_fmt)
```

此测试代码从 `structly` 包中导入必要的函数和类，创建每种类型的格式化器，定义一些测试数据，然后通过以相应格式打印数据来测试每个格式化器。

进行这些更改后，保存并退出文件。现在运行测试：

```bash
python test_tableformat.py
```

你应该会看到相同的数据以三种不同的方式（文本、CSV 和 HTML）进行格式化。如果你看到了预期的输出，这意味着你的代码重组成功了。
