# 添加一个工具栏

在应用程序中添加一个工具栏，允许用户进行放大、缩小、平移操作，以及将绘图保存为图像。此工具栏添加到框架的底部。

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```
