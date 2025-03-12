# 理解 Python 中的主模块

在 Python 中，当你直接运行一个脚本时，它会作为“主”模块。Python 有一个特殊的变量 `__name__`。当一个文件被直接执行时，Python 会将 `__name__` 的值设置为 `"__main__"`。这与该文件作为模块被导入时的情况不同。

这个特性非常有用，因为它允许你编写根据文件是直接运行还是被导入而表现不同的代码。例如，你可能希望某些代码仅在将文件作为脚本执行时运行，而在它被另一个脚本导入时不运行。

## 修改 `pcost.py` 以使用主模块模式

让我们修改 `pcost.py` 程序以利用这种模式。

1. 首先，你需要在编辑器中打开 `pcost.py` 文件。你可以使用以下命令导航到项目目录，并在文件不存在时创建它：

```bash
cd ~/project
touch pcost.py
```

`cd` 命令将当前目录更改为你主目录下的 `project` 目录。`touch` 命令会在 `pcost.py` 文件不存在时创建一个新的该文件。

2. 现在，将 `pcost.py` 文件修改为如下内容：

```python
# pcost.py

def portfolio_cost(filename):
    total_cost = 0.0

    with open(filename, 'r') as f:
        for line in f:
            fields = line.split()
            try:
                nshares = int(fields[1])
                price = float(fields[2])
                total_cost += nshares * price
            except (ValueError, IndexError):
                print(f"Couldn't parse: {line}")

    return total_cost

# 此代码仅在文件作为脚本执行时运行
if __name__ == "__main__":
    total = portfolio_cost('portfolio.dat')
    print(total)
```

这里的主要更改是，我们将末尾的代码包装在 `if __name__ == "__main__":` 条件语句中。这意味着该代码块内的代码仅在文件作为脚本直接执行时运行，而在它作为模块被导入时不运行。

3. 完成这些更改后，保存文件并退出编辑器。

## 测试修改后的模块

现在，让我们以两种不同的方式测试我们修改后的模块，看看它的表现如何。

1. 首先，使用以下命令将程序作为脚本直接运行：

```bash
python3 pcost.py
```

你应该会看到输出 `44671.15`，和之前一样。这是因为当你直接运行脚本时，`__name__` 变量被设置为 `"__main__"`，所以 `if __name__ == "__main__":` 代码块内的代码会被执行。

2. 接下来，再次启动 Python 解释器并导入该模块：

```bash
python3
```

```python
import pcost
```

这次，你不会看到任何输出。当你导入模块时，`__name__` 变量被设置为 `"pcost"`（模块名），而不是 `"__main__"`。因此，`if __name__ == "__main__":` 代码块内的代码不会运行。

3. 为了验证 `portfolio_cost` 函数仍然可以正常工作，你可以像这样调用它：

```python
pcost.portfolio_cost('portfolio.dat')
```

该函数应该返回 `44671.15`，这意味着它工作正常。

4. 最后，使用以下命令退出 Python 解释器：

```python
exit()
```

这种模式在创建既可以作为可导入模块又可以作为独立脚本使用的 Python 文件时非常有用。`if __name__ == "__main__":` 代码块内的代码仅在文件被直接执行时运行，而在它作为模块被导入时不运行。
