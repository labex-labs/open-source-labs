# 创建列表

使用方括号来定义列表字面量：

```python
names = [ 'Elwood', 'Jake', 'Curtis' ]
nums = [ 39, 38, 42, 65, 111]
```

有时列表是通过其他方法创建的。例如，可以使用 `split()` 方法将字符串拆分为列表：

```python
>>> line = 'GOOG,100,490.10'
>>> row = line.split(',')
>>> row
['GOOG', '100', '490.10']
>>>
```
