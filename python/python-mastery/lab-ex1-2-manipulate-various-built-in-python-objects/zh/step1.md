# 处理 Python 数字

Python 为数值运算提供了强大的支持。在编程中，数字是用于计算和表示数量的基本数据类型。本步骤将向你介绍 Python 中的基本数字操作，这对于在程序中执行各种数学运算至关重要。

## 基本算术运算

要开始处理 Python 数字，你首先需要打开一个 Python 交互式 shell。你可以在终端中输入 `python3` 来实现。Python 交互式 shell 允许你逐行编写和执行 Python 代码，这对于测试和学习非常有用。

```bash
python3
```

一旦进入 Python 交互式 shell，你就可以尝试一些基本的算术运算。Python 遵循标准的数学算术规则，例如运算顺序（PEMDAS：括号、指数、乘法和除法、加法和减法）。

```python
>>> 3 + 4*5    # 乘法的优先级高于加法，所以先计算 4*5，然后再加上 3
23
>>> 23.45 / 1e-02    # 这里使用了科学记数法表示 0.01。执行除法运算得到结果
2345.0
```

## 整数除法

Python 3 处理除法的方式与 Python 2 不同。理解这些差异对于避免代码中出现意外结果至关重要。

```python
>>> 7 / 4    # 在 Python 3 中，普通除法返回一个浮点数，即使结果可能是整数
1.75
>>> 7 // 4   # 整除（截断小数部分）会将商作为整数返回
1
```

## 数字方法

Python 中的数字有几个常被忽视的有用方法。这些方法可以简化复杂的数值运算和转换。让我们来探索其中一些：

```python
>>> x = 1172.5
>>> x.as_integer_ratio()    # 此方法将浮点数表示为分数，这在某些数学计算中很有用
(2345, 2)
>>> x.is_integer()    # 检查浮点数是否为整数值。在这种情况下，1172.5 不是整数，所以返回 False
False

>>> y = 12345
>>> y.numerator    # 对于整数，分子就是该数字本身
12345
>>> y.denominator    # 对于整数，分母始终为 1
1
>>> y.bit_length()    # 此方法告诉你用二进制表示该数字所需的位数，这在按位运算中很有用
14
```

当你需要执行特定的数值运算或转换时，这些方法特别有用。它们可以节省你的时间并使你的代码更高效。

当你完成对 Python 交互式 shell 的探索后，你可以通过输入以下内容退出：

```python
>>> exit()
```
