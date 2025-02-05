# 练习7.1：可变参数的简单示例

尝试定义以下函数：

```python
>>> def avg(x,*more):
        return float(x+sum(more))/(1+len(more))

>>> avg(10,11)
10.5
>>> avg(3,4,5)
4.0
>>> avg(1,2,3,4,5,6)
3.5
>>>
```

注意参数 `*more` 是如何收集所有额外参数的。
