# 添加文本箭头以指示方向

为了指示数据的方向，我们将使用 `ax.text()` 函数和 `bbox` 参数添加一个文本箭头，并将 `boxstyle` 设置为 “rarrow”。

```python
bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0, 0, "Direction", ha="center", va="center", rotation=45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)
```
