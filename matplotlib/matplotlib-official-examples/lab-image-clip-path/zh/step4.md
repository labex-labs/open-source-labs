# 创建补丁

为了创建补丁，我们将使用 Matplotlib 的 `patches` 模块。我们将创建一个半径为 200 像素的圆形补丁，圆心位于点 (260, 200) 处。

```python
patch = patches.Circle((260, 200), radius=200, transform=ax.transData)
```
