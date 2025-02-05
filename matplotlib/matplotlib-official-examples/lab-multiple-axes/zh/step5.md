# 绘制连接线

第五步是绘制一条连接两个子图的虚线。我们创建一个`ConnectionPatch`对象，它将左边子图的原点连接到右边子图的右边缘。我们还保存了`con`补丁对象，稍后将在动画中更新它。

```python
con = ConnectionPatch(
    (1, 0),
    (0, 0),
    "data",
    "data",
    axesA=axl,
    axesB=axr,
    color="C0",
    ls="dotted",
)
fig.add_artist(con)
```
