# 处理 Python 字符串

字符串是 Python 中最常用的数据类型之一。它们用于表示文本，可以包含字母、数字和符号。在这一步中，我们将探索各种字符串操作，这是在 Python 中处理文本数据的必备技能。

## 创建和定义字符串

要开始在 Python 中处理字符串，我们首先需要打开一个 Python 交互式 shell。这个 shell 允许我们逐行编写和执行 Python 代码，非常适合学习和测试。使用以下命令再次打开 Python 交互式 shell：

```bash
python3
```

shell 打开后，我们就可以定义一个字符串。在这个例子中，我们将创建一个包含股票代码的字符串。在 Python 中，字符串可以通过将文本用单引号 (`'`) 或双引号 (`"`) 括起来来定义。以下是我们定义字符串的方式：

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
>>> symbols
'AAPL IBM MSFT YHOO SCO'
```

现在我们已经创建了一个名为 `symbols` 的字符串变量，并为其赋值。当我们输入变量名并按下回车键时，Python 会显示字符串的值。

## 访问字符和子字符串

在 Python 中，可以通过索引来访问字符串中的单个字符。索引从 0 开始，这意味着字符串的第一个字符的索引为 0，第二个字符的索引为 1，依此类推。Python 也支持负索引，其中 -1 表示最后一个字符，-2 表示倒数第二个字符，依此类推。

让我们看看如何访问 `symbols` 字符串中的单个字符：

```python
>>> symbols[0]    # 第一个字符
'A'
>>> symbols[1]    # 第二个字符
'A'
>>> symbols[2]    # 第三个字符
'P'
>>> symbols[-1]   # 最后一个字符
'O'
>>> symbols[-2]   # 倒数第二个字符
'C'
```

我们还可以使用切片来提取子字符串。切片允许我们通过指定起始索引和结束索引来获取字符串的一部分。切片的语法是 `string[start:end]`，其中子字符串包含从起始索引到（但不包括）结束索引的字符。

```python
>>> symbols[:4]    # 前 4 个字符
'AAPL'
>>> symbols[-3:]   # 最后 3 个字符
'SCO'
>>> symbols[5:8]   # 从索引 5 到 7 的字符
'IBM'
```

## 字符串的不可变性

Python 中的字符串是不可变的，这意味着一旦创建了一个字符串，就不能更改其单个字符。如果你尝试修改字符串中的某个字符，Python 会引发错误。

让我们尝试更改 `symbols` 字符串的第一个字符：

```python
>>> symbols[0] = 'a'    # 这将导致错误
```

你应该会看到类似这样的错误：

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```

这个错误表明我们不能为字符串中的单个字符赋新值，因为字符串是不可变的。

## 字符串拼接

虽然我们不能直接修改字符串，但可以通过拼接来创建新的字符串。拼接是指将两个或多个字符串连接在一起。在 Python 中，我们可以使用 `+` 运算符来拼接字符串。

```python
>>> symbols += ' GOOG'    # 追加一个新的代码
>>> symbols
'AAPL IBM MSFT YHOO SCO GOOG'

>>> symbols = 'HPQ ' + symbols    # 前置一个新的代码
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

重要的是要记住，这些操作会创建新的字符串，而不是修改原始字符串。原始字符串保持不变，新的字符串是由组合后的值创建的。

## 测试子字符串

要检查一个子字符串是否存在于一个字符串中，我们可以使用 `in` 运算符。如果在字符串中找到子字符串，`in` 运算符返回 `True`，否则返回 `False`。

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
```

注意，'AA' 返回 `True`，因为它存在于 "AAPL" 中。这是在较大字符串中搜索特定文本的一种有用方法。

## 字符串方法

Python 字符串有许多内置方法，允许我们对字符串执行各种操作。这些方法是与字符串对象关联的函数，可以使用点号表示法 (`string.method()`) 调用。

```python
>>> symbols.lower()    # 转换为小写
'hpq aapl ibm msft yhoo sco goog'

>>> symbols    # 原始字符串保持不变
'HPQ AAPL IBM MSFT YHOO SCO GOOG'

>>> lowersyms = symbols.lower()    # 将结果保存到一个新变量中
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'

>>> symbols.find('MSFT')    # 查找子字符串的起始索引
13
>>> symbols[13:17]    # 验证该位置的子字符串
'MSFT'

>>> symbols = symbols.replace('SCO','')    # 替换子字符串
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
```

当你完成实验后，可以使用以下命令退出 Python shell：

```python
>>> exit()
```
