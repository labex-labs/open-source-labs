# 练习1.16：字符串方法

在Python交互式提示符下，尝试使用一些字符串方法。

```python
>>> symbols.lower()
?
>>> symbols
?
>>>
```

记住，字符串始终是只读的。如果你想保存操作结果，需要将其存储在变量中：

```python
>>> lowersyms = symbols.lower()
>>>
```

再尝试一些其他操作：

```python
>>> symbols.find('MSFT')
?
>>> symbols[13:17]
?
>>> symbols = symbols.replace('SCO','DOA')
>>> symbols
?
>>> name ='  IBM   \n'
>>> name = name.strip()    # 移除周围的空白字符
>>> name
?
>>>
```
