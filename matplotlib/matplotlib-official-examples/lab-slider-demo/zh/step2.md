# 定义正弦波函数

接下来，我们将定义生成正弦波的函数。该函数将接受两个参数，即幅度和频率，并返回给定时间的正弦波。

```python
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)
```
