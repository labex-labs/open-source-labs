# 创建茎叶图

接下来，我们将创建一个茎叶图，通过设置不同的高度来区分相近的事件。我们在基线上添加标记，以突出时间线的一维特性。对于每个事件，我们通过 `~.Axes.annotate` 添加一个文本标签，标签相对于事件线的顶端以点为单位进行偏移。以下是创建茎叶图的代码：

```python
# 选择一些合适的高度
levels = np.tile([-5, 5, -3, 3, -1, 1],
                 int(np.ceil(len(dates)/6)))[:len(dates)]

# 创建图形并绘制带有日期的茎叶图
fig, ax = plt.subplots(figsize=(8.8, 4), layout="constrained")
ax.set(title="Matplotlib release dates")

ax.vlines(dates, 0, levels, color="tab:red")  # 垂直的茎
ax.plot(dates, np.zeros_like(dates), "-o",
        color="k", markerfacecolor="w")  # 基线及其上的标记

# 为线条添加注释
for d, l, r in zip(dates, levels, names):
    ax.annotate(r, xy=(d, l),
                xytext=(-3, np.sign(l)*3), textcoords="offset points",
                horizontalalignment="right",
                verticalalignment="bottom" if l > 0 else "top")
```
