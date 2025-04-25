# 绘制一条对角线

首先，我们将使用 Matplotlib 的`plot()`函数绘制一条 45 度角的对角线。

```python
fig, ax = plt.subplots()

# 绘制对角线（45 度）
h = ax.plot(range(0, 10), range(0, 10))
```
