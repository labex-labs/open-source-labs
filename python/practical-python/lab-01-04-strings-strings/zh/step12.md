# 练习 1.13：提取单个字符和子字符串

字符串是字符数组。尝试提取几个字符：

```python
>>> symbols[0]
?
>>> symbols[1]
?
>>> symbols[2]
?
>>> symbols[-1]        # 最后一个字符
?
>>> symbols[-2]        # 负索引从字符串末尾开始
?
>>>
```

在 Python 中，字符串是只读的。

通过尝试将 `symbols` 的第一个字符改为小写的 'a' 来验证这一点。

```python
>>> symbols[0] = 'a'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError:'str' 对象不支持项赋值
>>>
```
