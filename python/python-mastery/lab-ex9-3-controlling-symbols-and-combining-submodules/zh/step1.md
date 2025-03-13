# 理解包导入的复杂性

当你开始使用 Python 包时，你很快就会意识到导入模块可能会变得相当复杂和冗长。这种复杂性会使你的代码更难读写。在这个实验中，我们将仔细研究这个问题，并学习如何简化导入过程。

## 当前的导入结构

首先，让我们打开终端。终端是一个强大的工具，它允许你与计算机的操作系统进行交互。终端打开后，我们需要导航到项目目录。项目目录是存储与我们的 Python 项目相关的所有文件的地方。为此，我们将使用 `cd` 命令，它代表 “change directory”（更改目录）。

```bash
cd ~/project
```

现在我们已经进入了项目目录，让我们来查看 `structly` 包的当前结构。Python 中的包是一种组织相关模块的方式。我们可以使用 `ls -la` 命令列出 `structly` 包内的所有文件和目录，包括隐藏文件。

```bash
ls -la structly
```

你会注意到 `structly` 包中有几个 Python 模块。这些模块包含我们可以在代码中使用的函数和类。然而，如果我们想使用这些模块中的功能，目前需要使用很长的导入语句。例如：

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

这些长导入路径写起来很麻烦，特别是如果你需要在代码中多次使用它们。它们还会使你的代码可读性降低，当你试图理解或调试代码时，这可能会成为一个问题。在这个实验中，我们将学习如何以一种使这些导入更简单的方式来组织包。

让我们先看看包的 `__init__.py` 文件的内容。`__init__.py` 文件是 Python 包中的一个特殊文件。当包被导入时，它会被执行，并且可以用来初始化包并设置任何必要的导入。

```bash
cat structly/__init__.py
```

你可能会发现 `__init__.py` 文件要么是空的，要么只包含很少的代码。在接下来的步骤中，我们将修改这个文件以简化我们的导入语句。

## 目标

在这个实验结束时，我们的目标是能够使用更简单的导入语句。与我们之前看到的长导入路径不同，我们将能够使用如下语句：

```python
from structly import Structure, read_csv_as_instances, create_formatter, print_table
```

甚至：

```python
from structly import *
```

使用这些更简单的导入语句将使我们的代码更简洁，更易于处理。在编写和维护代码时，它还能为我们节省时间和精力。
