# 创建图形1

我们将首先创建第一个图形，它将包含两个子图。我们将在顶部子图中绘制第一个正弦波，并在底部子图中绘制第一个正弦波幅度两倍的波形。

```python
plt.figure(1)

# 顶部子图
plt.subplot(211)
plt.plot(t, s1)

# 底部子图
plt.subplot(212)
plt.plot(t, 2*s1)
```
