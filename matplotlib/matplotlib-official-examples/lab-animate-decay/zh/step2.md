# 创建数据生成函数

接下来，我们需要创建一个函数来生成动画所需的数据。该函数将生成一个随时间衰减的正弦波。我们将使用 `itertools.count()` 函数生成一个无限的数字序列。我们将使用这些数字来计算正弦波的值。

```python
def data_gen():
    for cnt in itertools.count():
        t = cnt / 10
        yield t, np.sin(2*np.pi*t) * np.exp(-t/10.)
```
