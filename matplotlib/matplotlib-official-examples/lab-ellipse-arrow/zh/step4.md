# 反转方向箭头

如果你想反转方向箭头，可以将标记类型从 `>` 切换为 `<`。

```python
# 要反转方向箭头，将标记类型从 > 切换为 <。
ax.plot(
    vertices[0][0],
    vertices[0][1],
    color="b",
    marker=MarkerStyle("<", "full", t),
    markersize=10
)
```
