# 可视化t-SNE结果

最后，我们可以使用散点图来可视化t-SNE的结果。

```python
ax = plt.subplot(1, 1, 1)
ax.scatter(Y[red, 0], Y[red, 1], c="r")
ax.scatter(Y[green, 0], Y[green, 1], c="g")
ax.xaxis.set_major_formatter(NullFormatter())
ax.yaxis.set_major_formatter(NullFormatter())
plt.axis("tight")
```
