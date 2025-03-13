# 创建包结构

现在，我们要创建 Python 包了。但首先，让我们了解一下什么是 Python 包。Python 包是一种将相关 Python 模块组织到单个目录层次结构中的方式。它有助于更有效地管理和复用代码。要创建 Python 包，我们需要遵循以下步骤：

1. 创建一个以包名命名的目录。这个目录将作为属于该包的所有模块的容器。
2. 在这个目录中创建一个 `__init__.py` 文件。这个文件至关重要，因为它能让 Python 将该目录识别为一个包。当你导入这个包时，`__init__.py` 中的代码会被执行，可用于初始化该包。
3. 将我们的 Python 模块文件移动到这个目录中。这一步确保所有相关代码都被分组在包内。

让我们逐步创建包结构：

1. 首先，创建一个名为 `structly` 的目录。这将是我们包的根目录。

```bash
mkdir structly
```

2. 接下来，在 `structly` 目录中创建一个空的 `__init__.py` 文件。

```bash
touch structly/__init__.py
```

`__init__.py` 文件可以为空，但要让 Python 将该目录视为一个包，它是必需的。当你导入这个包时，`__init__.py` 中的代码会被执行，可用于初始化该包。

3. 现在，让我们把 Python 模块文件移动到 `structly` 目录中。这些模块文件包含了我们想要包含在包中的函数和类。

```bash
mv structure.py validate.py reader.py tableformat.py structly/
```

4. 验证所有文件是否已正确移动。我们可以使用 `ls -l` 命令列出 `structly` 目录的内容。

```bash
ls -l structly/
```

你应该会看到列出以下文件：

```
__init__.py
reader.py
structure.py
tableformat.py
validate.py
```

现在我们已经创建了一个基本的包结构。目录层次结构应该如下所示：

```
project/
├── portfolio.csv
├── stock.py
└── structly/
    ├── __init__.py
    ├── reader.py
    ├── structure.py
    ├── tableformat.py
    └── validate.py
```

下一步，我们将修正导入语句，以使包能正常工作。
