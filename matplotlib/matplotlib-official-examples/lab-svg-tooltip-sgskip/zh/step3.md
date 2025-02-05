# 将图形保存为 SVG

我们使用 `BytesIO` 类和 `savefig` 方法将图形保存到一个虚拟文件对象中。

```python
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)
ax.set_aspect('equal')

f = BytesIO()
plt.savefig(f, format="svg")
```
