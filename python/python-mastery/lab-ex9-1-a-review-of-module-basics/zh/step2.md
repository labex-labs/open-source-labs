# 导入和使用模块

既然我们已经创建了一个模块，现在是时候了解如何导入它并使用其组件了。在 Python 中，模块是包含 Python 定义和语句的文件。当你导入一个模块时，你可以访问其中定义的所有函数、类和变量。这使你能够重用代码并更有效地组织程序。

1. 首先，我们需要在 WebIDE 中打开一个新的终端。这个终端将作为我们运行 Python 命令的工作空间。要打开新终端，请点击 “Terminal” > “New Terminal”。

2. 终端打开后，我们需要启动 Python 解释器。Python 解释器是一个读取并执行 Python 代码的程序。要启动它，请在终端中输入以下命令并按回车键：

```bash
python3
```

3. 现在 Python 解释器已经运行，我们可以导入我们的模块了。在 Python 中，我们使用 `import` 语句将模块引入到当前程序中。在 Python 解释器中输入以下命令：

```python
>>> import simplemod
Loaded simplemod
```

你会注意到输出中出现了 “Loaded simplemod”。这是因为我们的 `simplemod` 模块中的 `print` 语句在模块加载时会执行。当 Python 导入一个模块时，它会运行该模块中的所有顶级代码，包括任何 `print` 语句。

4. 导入模块后，我们可以使用点号表示法来访问其组件。点号表示法是 Python 中访问对象属性（变量和函数）的一种方式。在这种情况下，模块就是一个对象，其函数、变量和类就是它的属性。以下是一些如何访问 `simplemod` 模块不同组件的示例：

```python
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
>>> spam_instance = simplemod.Spam()
>>> spam_instance.yow()
Yow!
```

第一行中，我们访问了 `simplemod` 模块中定义的变量 `x`。第二行中，我们调用了 `simplemod` 模块中的函数 `foo`。第三行和第四行中，我们创建了 `simplemod` 模块中定义的 `Spam` 类的一个实例，并调用了其方法 `yow`。

5. 有时，你在尝试导入模块时可能会遇到 `ImportError`。当 Python 找不到你要导入的模块时，就会出现这个错误。要确定 Python 在哪里查找模块，你可以检查 `sys.path` 变量。`sys.path` 变量是一个目录列表，Python 在查找模块时会搜索这些目录。在 Python 解释器中输入以下命令：

```python
>>> import sys
>>> sys.path
['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
```

列表中的第一个元素（空字符串）表示当前工作目录。这就是 Python 查找 `simplemod.py` 文件的地方。如果你的模块不在 `sys.path` 列出的任何一个目录中，Python 将无法找到它，你就会得到一个 `ImportError`。确保你的 `simplemod.py` 文件位于当前工作目录或 `sys.path` 中的其他目录之一。
