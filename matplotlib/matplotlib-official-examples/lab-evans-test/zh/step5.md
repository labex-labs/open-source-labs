# 创建数据点

在这一步中，我们将使用自定义单位类——`Foo`——创建一些数据点。

```python
# 创建一些 Foo 对象
x = [Foo(val, 1.0) for val in range(0, 50, 2)]
# 以及一些任意的 y 数据
y = [i for i in range(len(x))]
```
