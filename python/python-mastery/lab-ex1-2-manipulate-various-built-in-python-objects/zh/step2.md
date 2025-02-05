# 第2部分：字符串操作

定义一个包含一系列股票代码的字符串，如下所示：

```python
>>> symbols = 'AAPL IBM MSFT YHOO SCO'
```

现在，让我们尝试不同的字符串操作：

## 提取单个字符和子字符串

字符串是字符数组。尝试提取几个字符：

```python
>>> symbols[0]
'A'
>>> symbols[1]
'A'
>>> symbols[2]
'P'
>>> symbols[-1]        # 最后一个字符
'O'
>>> symbols[-2]        # 倒数第二个字符
'C'
>>>
```

尝试进行一些切片操作：

```python
>>> symbols[:4]
'AAPL'
>>> symbols[-3:]
'SCO'
>>> symbols[5:8]
'IBM'
>>>
```

## 字符串作为只读对象

字符串是只读的。通过尝试将 `symbols` 的第一个字符更改为小写的 'a' 来验证这一点。

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
>>>
```

## 字符串拼接

虽然字符串数据是只读的，但你始终可以将变量重新赋值为新创建的字符串。
尝试以下语句，将新的代码 "GOOG" 拼接到 `symbols` 的末尾：

```python
>>> symbols += ' GOOG'
>>> symbols
... 查看结果...
```

现在，尝试像这样将 "HPQ" 添加到 `symbols` 的开头：

```python
>>> symbols = 'HPQ'+ symbols
>>> symbols
... 查看结果...
```

在这两个示例中都应注意，原始字符串 `symbols` 并未在原地被修改。相反，会创建一个全新的字符串。变量名 `symbols` 只是绑定到结果。之后，旧字符串会被销毁，因为不再使用它了。

## 成员测试（子字符串测试）

使用 `in` 运算符来检查子字符串。在交互式提示符下，尝试这些操作：

```python
>>> 'IBM' in symbols
True
>>> 'AA' in symbols
True
>>> 'CAT' in symbols
False
>>>
```

确保你理解为什么对 "AA" 的检查返回 `True`。

## 字符串方法

在Python交互式提示符下，尝试使用一些字符串方法。

```python
>>> symbols.lower()
'hpq aapl ibm msft yhoo sco goog'
>>> symbols
'HPQ AAPL IBM MSFT YHOO SCO GOOG'
```

请记住，字符串始终是只读的。如果你想保存操作结果，需要将其放入变量中：

```python
>>> lowersyms = symbols.lower()
>>> lowersyms
'hpq aapl ibm msft yhoo sco goog'
>>>
```

尝试更多操作：

```python
>>> symbols.find('MSFT')
13
>>> symbols[13:17]
'MSFT'
>>> symbols = symbols.replace('SCO','')
>>> symbols
'HPQ AAPL IBM MSFT YHOO  GOOG'
>>>
```
