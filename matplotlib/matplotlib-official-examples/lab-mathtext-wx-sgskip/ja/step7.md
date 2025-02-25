# ツールバーを追加する

ユーザーがズームイン・アウト、パン操作を行い、グラフを画像として保存できるようにするツールバーをアプリケーションに追加します。このツールバーはフレームの下部に追加されます。

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```
