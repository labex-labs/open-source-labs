# 字符串的不可变性

字符串是“不可变的”，即只读的。一旦创建，其值就不能被更改。

```python
>>> s = 'Hello World'
>>> s[1] = 'a'
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError:'str' object does not support item assignment
>>>
```

**所有操作和处理字符串数据的方法，总是会创建新的字符串。**
