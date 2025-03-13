# 使用 `__all__` 控制导出的符号

在 Python 中，当你使用 `from module import *` 语句时，你可能希望控制从模块中导入哪些符号（函数、类、变量）。这就是 `__all__` 变量发挥作用的地方。`from module import *` 语句是一种将模块中的所有符号导入到当前命名空间的方式。然而，有时你并不想导入每个符号，特别是当符号很多或者有些符号是模块内部使用的时候。`__all__` 变量允许你精确指定使用该语句时应导入哪些符号。

## 什么是 `__all__`？

`__all__` 变量是一个字符串列表。这个列表中的每个字符串代表一个符号（函数、类或变量），当有人使用 `from module import *` 语句时，模块会导出这些符号。如果模块中未定义 `__all__` 变量，`import *` 语句将导入所有不以下划线开头的符号。以下划线开头的符号通常被视为模块的私有或内部符号，不应该直接导入。

## 修改每个子模块

现在，让我们将 `__all__` 变量添加到 `structly` 包的每个子模块中。这将帮助我们控制当有人使用 `from module import *` 语句时，每个子模块导出哪些符号。

1. 首先，让我们修改 `structure.py`：

```bash
touch ~/project/structly/structure.py
```

此命令在你的项目的 `structly` 目录中创建一个名为 `structure.py` 的新文件。创建文件后，我们需要添加 `__all__` 变量。在文件顶部，紧接在导入语句之后添加以下行：

```python
__all__ = ['Structure']
```

这行代码告诉 Python，当有人使用 `from structure import *` 时，仅会导入 `Structure` 符号。保存文件并退出编辑器。

2. 接下来，让我们修改 `reader.py`：

```bash
touch ~/project/structly/reader.py
```

此命令在 `structly` 目录中创建一个名为 `reader.py` 的新文件。现在，浏览文件，找出所有以 `read_csv_as_` 开头的函数。这些函数就是我们想要导出的函数。然后，添加一个包含所有这些函数名的 `__all__` 列表。它应该类似于以下内容：

```python
__all__ = ['read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns']
```

请注意，实际的函数名可能会根据你在文件中找到的内容而有所不同。确保包含你找到的所有 `read_csv_as_*` 函数。保存文件并退出编辑器。

3. 现在，让我们修改 `tableformat.py`：

```bash
touch ~/project/structly/tableformat.py
```

此命令在 `structly` 目录中创建一个名为 `tableformat.py` 的新文件。在文件顶部附近添加以下行：

```python
__all__ = ['create_formatter', 'print_table']
```

这行代码指定，当有人使用 `from tableformat import *` 时，仅会导入 `create_formatter` 和 `print_table` 符号。保存文件并退出编辑器。

## 在 `__init__.py` 中统一导入

现在每个模块都定义了它要导出的内容，我们可以更新 `__init__.py` 文件以导入所有这些符号。`__init__.py` 文件是 Python 包中的一个特殊文件。当包被导入时，它会被执行，并且可以用来初始化包并从子模块导入符号。

```bash
touch ~/project/structly/__init__.py
```

此命令在 `structly` 目录中创建一个新的 `__init__.py` 文件。将文件内容更改为：

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *
```

这些行从 `structure`、`reader` 和 `tableformat` 子模块导入所有导出的符号。模块名前的点 (`.`) 表示这些是相对导入，即从同一包内进行导入。保存文件并退出编辑器。

## 测试我们的更改

让我们创建一个简单的测试文件来验证我们的更改是否有效。这个测试文件将尝试导入我们在 `__all__` 变量中指定的符号，如果导入成功，则打印一条成功消息。

```bash
touch ~/project/test_structly.py
```

此命令在项目目录中创建一个名为 `test_structly.py` 的新文件。将以下内容添加到文件中：

```python
# A simple test to verify our imports work correctly

from structly import Structure
from structly import read_csv_as_instances
from structly import create_formatter, print_table

print("Successfully imported all required symbols!")
```

这些行尝试从 `structly` 包中导入 `Structure` 类、`read_csv_as_instances` 函数以及 `create_formatter` 和 `print_table` 函数。如果导入成功，程序将打印消息 “Successfully imported all required symbols!”。保存文件并退出编辑器。现在让我们运行这个测试：

```bash
cd ~/project
python test_structly.py
```

`cd ~/project` 命令将当前工作目录更改为项目目录。`python test_structly.py` 命令运行 `test_structly.py` 脚本。如果一切正常，你应该会在屏幕上看到消息 “Successfully imported all required symbols!”。
