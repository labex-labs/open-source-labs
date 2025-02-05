# 将各行拆分为列

`delimiter` 参数用于定义各行应如何拆分为列。默认情况下，`numpy.genfromtxt` 假定 `delimiter=None`，这意味着该行将按空白字符（包括制表符）进行拆分。

```python
np.genfromtxt(StringIO(data), delimiter=",")
```
