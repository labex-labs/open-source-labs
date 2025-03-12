# 理解函数参数传递

在 Python 中，函数是一个基本概念，它允许你将一组语句组合在一起以执行特定任务。当你调用一个函数时，通常需要为其提供一些数据，我们将这些数据称为参数。Python 提供了不同的方式将这些参数传递给函数。这种灵活性非常有用，因为它有助于你编写更简洁、更易维护的代码。在将这些技术应用到我们的项目之前，让我们仔细了解一下这些参数传递约定。

## 备份你的工作

在开始对 `stock.py` 文件进行修改之前，创建一个备份是个好习惯。这样，如果在实验过程中出现问题，我们总能恢复到原始版本。要创建备份，请打开终端并运行以下命令：

```bash
cp stock.py orig_stock.py
```

此命令使用终端中的 `cp`（复制）命令。它将 `stock.py` 文件复制一份，命名为 `orig_stock.py`。通过这样做，我们确保原始工作得到了安全保存。

## 探索函数参数传递

在 Python 中，有几种不同类型的参数调用函数的方法。让我们详细探讨每种方法。

### 1. 位置参数

将参数传递给函数的最简单方法是按位置传递。当你定义一个函数时，需要指定一个参数列表。调用函数时，要按照定义的顺序为这些参数提供值。

以下是一个示例：

```python
def calculate(x, y, z):
    return x + y + z

# Call with positional arguments
result = calculate(1, 2, 3)
print(result)  # Output: 6
```

在这个示例中，`calculate` 函数接受三个参数：`x`、`y` 和 `z`。当我们使用 `calculate(1, 2, 3)` 调用该函数时，值 `1` 被赋给 `x`，`2` 被赋给 `y`，`3` 被赋给 `z`。然后函数将这些值相加并返回结果。

### 2. 关键字参数

除了位置参数，你还可以通过参数名来指定参数。这称为使用关键字参数。使用关键字参数时，你不必担心参数的顺序。

以下是一个示例：

```python
# Call with a mix of positional and keyword arguments
result = calculate(1, z=3, y=2)
print(result)  # Output: 6
```

在这个示例中，我们首先为 `x` 传递位置参数 `1`。然后，使用关键字参数为 `y` 和 `z` 指定值。只要提供了正确的名称，关键字参数的顺序无关紧要。

### 3. 解包序列和字典

Python 提供了一种方便的方式，使用 `*` 和 `**` 语法将序列和字典作为参数传递。这称为解包。

以下是将元组解包为位置参数的示例：

```python
# Unpacking a tuple into positional arguments
args = (1, 2, 3)
result = calculate(*args)
print(result)  # Output: 6
```

在这个示例中，我们有一个包含值 `1`、`2` 和 `3` 的元组 `args`。当我们在函数调用中在 `args` 前使用 `*` 运算符时，Python 会解包该元组，并将其元素作为位置参数传递给 `calculate` 函数。

以下是将字典解包为关键字参数的示例：

```python
# Unpacking a dictionary into keyword arguments
kwargs = {'y': 2, 'z': 3}
result = calculate(1, **kwargs)
print(result)  # Output: 6
```

在这个示例中，我们有一个包含键值对 `'y': 2` 和 `'z': 3` 的字典 `kwargs`。当我们在函数调用中在 `kwargs` 前使用 `**` 运算符时，Python 会解包该字典，并将其键值对作为关键字参数传递给 `calculate` 函数。

### 4. 接受可变参数

有时，你可能想定义一个可以接受任意数量参数的函数。Python 允许你在函数定义中使用 `*` 和 `**` 语法来实现这一点。

以下是一个接受任意数量位置参数的函数示例：

```python
# Accept any number of positional arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2))           # Output: 3
print(sum_all(1, 2, 3, 4, 5))  # Output: 15
```

在这个示例中，`sum_all` 函数使用 `*args` 参数来接受任意数量的位置参数。`*` 运算符将所有位置参数收集到一个名为 `args` 的元组中。然后，函数使用内置的 `sum` 函数将元组中的所有元素相加。

以下是一个接受任意数量关键字参数的函数示例：

```python
# Accept any number of keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Python", year=1991)
# Output:
# name: Python
# year: 1991
```

在这个示例中，`print_info` 函数使用 `**kwargs` 参数来接受任意数量的关键字参数。`**` 运算符将所有关键字参数收集到一个名为 `kwargs` 的字典中。然后，函数遍历字典中的键值对并将它们打印出来。

这些技术将帮助我们在接下来的步骤中创建更灵活、可复用的代码结构。为了更熟悉这些概念，让我们打开 Python 解释器并尝试一些上述示例。

```bash
python3
```

进入 Python 解释器后，尝试输入上述示例。这将让你亲身体验这些参数传递技术。
