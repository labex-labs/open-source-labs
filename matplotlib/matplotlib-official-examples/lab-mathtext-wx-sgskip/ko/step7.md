# 툴바 추가

사용자가 확대/축소, 이동 (pan) 및 플롯을 이미지로 저장할 수 있도록 하는 툴바를 애플리케이션에 추가합니다. 이 툴바는 프레임 하단에 추가됩니다.

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```
