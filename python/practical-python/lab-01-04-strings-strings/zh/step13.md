# 练习1.14：字符串拼接

虽然字符串数据是只读的，但你总是可以将变量重新赋值为新创建的字符串。

尝试以下语句，将新符号“GOOG”拼接到 `symbols` 的末尾：

```python
>>> symbols = symbols + 'GOOG'
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCOGOOG'
>>>
```

哎呀！这不是你想要的。修正它，使 `symbols` 变量的值为 `'AAPL,IBM,MSFT,YHOO,SCO,GOOG'`。

```python
>>> symbols =?
>>> symbols
'AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

在字符串开头添加 `'HPQ'`：

```python
>>> symbols =?
>>> symbols
'HPQ,AAPL,IBM,MSFT,YHOO,SCO,GOOG'
>>>
```

在这些示例中，看起来原始字符串好像被修改了，这显然违反了字符串只读的特性。其实并非如此。每次对字符串进行操作都会创建一个全新的字符串。当变量名 `symbols` 被重新赋值时，它指向新创建的字符串。之后，旧字符串会因为不再被使用而被销毁。
