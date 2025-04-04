# 理解 Python 包

在开始创建 Python 包之前，让我们先了解一下什么是 Python 包。Python 包本质上是一个目录。在这个目录中，有多个 Python 模块文件，也就是包含 Python 代码的 `.py` 文件。此外，还有一个名为 `__init__.py` 的特殊文件。这个文件可以为空，但它的存在表明该目录是一个 Python 包。这种结构的目的是帮助你将相关代码组织到一个单一的目录层次结构中。

包有几个优点。首先，它们允许你对代码进行逻辑组织。你可以将相关功能组合在一个包中，而不是让所有 Python 文件分散在各处。其次，它们有助于避免模块之间的命名冲突。由于包创建了一个命名空间，你可以在不同的包中使用同名的模块而不会有任何问题。第三，它们使导入和使用你的代码更加方便。你可以轻松地导入整个包或其中的特定模块。

现在，让我们看看项目目录中目前有的文件。要列出这些文件，我们将在终端中使用以下命令：

```bash
ls -l
```

当你运行这个命令时，你应该会看到以下文件：

```
portfolio.csv
reader.py
stock.py
structure.py
tableformat.py
validate.py
```

这些 Python 文件都是相关的，并且可以协同工作，但目前它们只是独立的模块。在这个实验中，我们的目标是将它们组织成一个名为 `structly` 的连贯包。

让我们简要了解一下每个文件的作用：

- `structure.py`：这个文件定义了一个基类 `Structure` 和各种描述符。这些描述符用于类型验证，即它们有助于确保程序中使用的数据具有正确的类型。
- `validate.py`：它包含 `structure` 模块使用的验证功能。这有助于根据特定规则验证数据。
- `reader.py`：这个文件提供了用于读取 CSV 数据的函数。CSV（逗号分隔值）是一种常见的用于存储表格数据的文件格式。
- `tableformat.py`：它包含用于将数据格式化为表格的类和函数。当你想以更有条理的方式显示数据时，这很有用。
- `stock.py`：这个文件使用其他模块来定义 `Stock` 类并处理股票数据。它结合了其他模块的功能来执行与股票数据相关的特定任务。

下一步，我们将创建包结构。
