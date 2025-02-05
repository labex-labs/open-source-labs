# 创建绘图

现在，我们将使用 `plt.subplots` 函数创建三个子图。其中两个图将在一个图形中创建，而第三个图将在单独的图形中创建。

```python
fig, (ax1, ax2) = plt.subplots(2, sharex=True)
ax1.plot(t, s1)
ax2.plot(t, s2)
fig, ax3 = plt.subplots()
ax3.plot(t, s3)
```
