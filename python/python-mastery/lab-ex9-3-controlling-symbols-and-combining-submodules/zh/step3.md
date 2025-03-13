# 从包中导出所有内容

在 Python 中，包的组织对于有效管理代码至关重要。现在，我们将进一步完善包的组织。我们将定义在包级别应该导出哪些符号。导出符号意味着让某些函数、类或变量可供代码的其他部分或可能使用你包的其他开发者使用。

## 向包中添加 `__all__`

当你使用 Python 包时，你可能希望控制当有人使用 `from structly import *` 语句时哪些符号是可访问的。这就是 `__all__` 列表发挥作用的地方。通过在包的 `__init__.py` 文件中添加一个 `__all__` 列表，你可以精确控制当有人使用 `from structly import *` 语句时哪些符号是可用的。

首先，让我们创建或更新 `__init__.py` 文件。如果文件不存在，我们将使用 `touch` 命令来创建它。

```bash
touch ~/project/structly/__init__.py
```

现在，打开 `__init__.py` 文件并添加一个 `__all__` 列表。这个列表应该包含我们想要导出的所有符号。这些符号根据它们的来源进行分组，例如 `structure`、`reader` 和 `tableformat` 模块。

```python
# structly/__init__.py

from .structure import *
from .reader import *
from .tableformat import *

# Define what symbols are exported when using "from structly import *"
__all__ = ['Structure',  # from structure
           'read_csv_as_instances', 'read_csv_as_dicts', 'read_csv_as_columns',  # from reader
           'create_formatter', 'print_table']  # from tableformat
```

添加代码后，保存文件并退出编辑器。

## 理解 `import *`

在大多数 Python 代码中，通常不建议使用 `from module import *` 模式。这有几个原因：

1. 它可能会用意外的符号污染你的命名空间。这意味着你的当前命名空间中可能会出现你意想不到的变量或函数，这可能会导致命名冲突。
2. 它会使特定符号的来源不明确。当你使用 `import *` 时，很难判断一个符号来自哪个模块，这会使你的代码更难理解和维护。
3. 它可能会导致遮蔽问题。当局部变量或函数与另一个模块中的变量或函数同名时，就会发生遮蔽，这可能会导致意外的行为。

然而，在特定情况下，使用 `import *` 是合适的：

- 对于设计为作为一个整体使用的包。如果一个包旨在作为一个单一单元使用，那么使用 `import *` 可以更方便地访问所有必要的符号。
- 当一个包通过 `__all__` 定义了清晰的接口时。通过使用 `__all__` 列表，你可以控制导出哪些符号，从而更安全地使用 `import *`。
- 对于交互式使用，例如在 Python REPL（读取 - 求值 - 打印循环）中。在交互式环境中，一次性导入所有符号可能会很方便。

## 使用 `import *` 进行测试

为了验证我们可以一次性导入所有符号，让我们创建另一个测试文件。我们将使用 `touch` 命令来创建文件。

```bash
touch ~/project/test_import_all.py
```

现在，打开 `test_import_all.py` 文件并添加以下内容。这段代码从 `structly` 包中导入所有符号，然后测试一些重要的符号是否可用。

```python
# Test importing everything at once

from structly import *

# Try using the imported symbols
print(f"Structure symbol is available: {Structure is not None}")
print(f"read_csv_as_instances symbol is available: {read_csv_as_instances is not None}")
print(f"create_formatter symbol is available: {create_formatter is not None}")
print(f"print_table symbol is available: {print_table is not None}")

print("All symbols successfully imported!")
```

保存文件并退出编辑器。现在，让我们运行测试。首先，使用 `cd` 命令导航到项目目录，然后运行 Python 脚本。

```bash
cd ~/project
python test_import_all.py
```

如果一切设置正确，你应该会看到确认所有符号都已成功导入的信息。
