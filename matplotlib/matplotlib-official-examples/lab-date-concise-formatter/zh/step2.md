# 简洁日期格式化器

接下来，我们探索 `~.dates.ConciseDateFormatter` 及其输出。我们使用简洁日期格式化器创建一个新的图表，并观察它与默认格式化器有何不同。

```python
fig, axs = plt.subplots(3, 1, layout='constrained', figsize=(6, 6))
for nn, ax in enumerate(axs):
    locator = mdates.AutoDateLocator(minticks=3, maxticks=7)
    formatter = mdates.ConciseDateFormatter(locator)
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)

    ax.plot(dates, y)
    ax.set_xlim(lims[nn])
axs[0].set_title('简洁日期格式化器')
plt.show()
```
