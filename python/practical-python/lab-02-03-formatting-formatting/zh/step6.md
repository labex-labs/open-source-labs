# 练习2.8：如何格式化数字

打印数字时常见的一个问题是指定小数位数。解决这个问题的一种方法是使用f字符串。试试这些示例：

```python
>>> value = 42863.1
>>> print(value)
42863.1
>>> print(f'{value:0.4f}')
42863.1000
>>> print(f'{value:>16.2f}')
        42863.10
>>> print(f'{value:<16.2f}')
42863.10
>>> print(f'{value:*>16,.2f}')
*******42,863.10
>>>
```

有关f字符串中使用的格式化代码的完整文档可在[此处](https://docs.python.org/3/library/string.html#format-specification-mini-language)找到。格式化有时也使用字符串的`%`运算符来执行。

```python
>>> print('%0.4f' % value)
42863.1000
>>> print('%16.2f' % value)
        42863.10
>>>
```

有关与`%`一起使用的各种代码的文档可在[此处](https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting)找到。

虽然它通常与`print`一起使用，但字符串格式化并不局限于打印。如果你想保存格式化后的字符串，只需将其赋给一个变量。

```python
>>> f = '%0.4f' % value
>>> f
'42863.1000'
>>>
```
