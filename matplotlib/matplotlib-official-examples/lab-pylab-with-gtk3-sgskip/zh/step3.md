# 访问工具栏和垂直框

我们将分别使用 `manager.toolbar` 和 `manager.vbox` 方法来访问图形画布管理器的工具栏和垂直框属性。

```python
manager = fig.canvas.manager
toolbar = manager.toolbar
vbox = manager.vbox
```
