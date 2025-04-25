# 练习 2.19：列表推导式

尝试一些简单的列表推导式，只是为了熟悉其语法。

```python
>>> nums = [1,2,3,4]
>>> squares = [ x * x for x in nums ]
>>> squares
[1, 4, 9, 16]
>>> twice = [ 2 * x for x in nums if x > 2 ]
>>> twice
[6, 8]
>>>
```

注意列表推导式是如何通过对数据进行适当的转换或过滤来创建一个新列表的。
