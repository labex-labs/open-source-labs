# 生成信号

接下来，我们将生成一个用于绘制的信号。在这个例子中，我们将创建一个由两个不同频率的正弦波与一些随机噪声相加得到的信号。

```python
# 固定随机状态以确保可重复性
np.random.seed(19680801)

dt = 0.0005
t = np.arange(0.0, 20.0, dt)
s1 = np.sin(2 * np.pi * 100 * t)
s2 = 2 * np.sin(2 * np.pi * 400 * t)

# 创建一个瞬态“啁啾”
s2[t <= 10] = s2[12 <= t] = 0

# 加入一些噪声
nse = 0.01 * np.random.random(size=len(t))

x = s1 + s2 + nse  # 信号
```
