# 绘制一条对角线

首先，我们将使用Matplotlib的`plot()`函数绘制一条45度角的对角线。

```python
fig, ax = plt.subplots()

# 绘制对角线（45度）
h = ax.plot(range(0, 10), range(0, 10))
```
