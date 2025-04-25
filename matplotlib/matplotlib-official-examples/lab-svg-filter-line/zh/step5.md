# 设置坐标轴范围并保存图形

我们设置坐标轴的 x 和 y 范围，并使用 `io.BytesIO()` 和 `plt.savefig()` 将图形保存为 SVG 格式的字节字符串。

```python
ax.set_xlim(0., 1.)
ax.set_ylim(0., 1.)

f = io.BytesIO()
plt.savefig(f, format="svg")
```
