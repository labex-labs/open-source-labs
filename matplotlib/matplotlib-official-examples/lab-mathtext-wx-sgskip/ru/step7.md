# Добавьте панель инструментов

Добавьте панель инструментов в приложение, которая позволяет пользователю приближать и удалять, перемещать и сохранять график в виде изображения. Эта панель инструментов добавляется в нижнюю часть рамки.

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```
