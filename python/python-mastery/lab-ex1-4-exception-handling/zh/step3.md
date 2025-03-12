# 交互式实验

Python 提供了一种交互式模式，让你可以立即运行代码。这对于测试代码和尝试新功能非常有用。在这一步中，我们将学习如何直接从 Python 解释器调用函数。

## 以交互式模式运行 Python

要运行 Python 脚本并进入交互式模式，你可以使用 `-i` 标志。这个标志告诉 Python 在执行脚本后保持交互式状态。以下是具体操作方法：

```bash
cd /home/labex/project
python3 -i pcost.py
```

让我们来分析一下这个命令的作用：

1. 首先，`cd /home/labex/project` 将当前目录更改为 `/home/labex/project`。这是我们的 `pcost.py` 脚本所在的位置。
2. 然后，`python3 -i pcost.py` 执行 `pcost.py` 脚本。脚本运行完成后，Python 会保持在交互式模式。
3. 在交互式模式下，你可以直接在终端中输入 Python 命令。

运行该命令后，你会看到 `pcost.py` 脚本的输出，随后是 Python 提示符 (`>>>`)。这个提示符表示你现在可以输入 Python 命令了。

## 交互式调用函数

进入交互式模式后，你可以使用不同的文件名调用 `portfolio_cost()` 函数。这能让你了解该函数在不同输入下的行为。以下是一个示例：

```python
>>> portfolio_cost('/home/labex/project/portfolio.dat')
44671.15
>>> portfolio_cost('/home/labex/project/portfolio2.dat')
19908.75
>>> portfolio_cost('/home/labex/project/portfolio3.dat')
Couldn't parse: 'C - 53.08
'
Reason: invalid literal for int() with base 10: '-'
Couldn't parse: 'DIS - 34.20
'
Reason: invalid literal for int() with base 10: '-'
44671.15
```

通过这种交互式方法，你可以：

- 使用不同的输入测试函数，查看其是否按预期工作。
- 试验函数在各种条件下的行为。
- 通过查看函数调用的即时结果，即时调试代码。

## 交互式模式的优点

交互式模式有几个优点：

1. 你可以快速测试不同的场景，而无需每次都运行整个脚本。
2. 你可以立即检查变量和表达式的结果，这有助于你理解代码的运行情况。
3. 你可以测试小段代码，而无需创建完整的程序。这对于学习和尝试新想法非常有用。
4. 这是学习和试验 Python 的绝佳方式，因为你能得到即时反馈。

## 退出交互式模式

当你完成实验后，可以通过两种方式退出交互式模式：

- 输入 `exit()` 并按回车键。这是结束交互式会话的直接方法。
- 按 Ctrl+D（在 Unix/Linux 系统上）。这是一个快捷键，也可以退出交互式模式。

在你的 Python 编程之旅中，定义函数并交互式测试它们的技术对于开发和调试将非常有价值。它能让你快速迭代代码，发现并修复问题。
