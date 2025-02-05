# 更新状态栏

最后，我们将定义一个方法，以便每当鼠标在绘图上移动时，用光标位置更新状态栏。

```python
def UpdateStatusBar(self, event):
    if event.inaxes:
        self.statusBar.SetStatusText(f"x={event.xdata}  y={event.ydata}")
```
