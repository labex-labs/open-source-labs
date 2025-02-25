# Fügen Sie eine Symbolleiste hinzu

Fügen Sie einer Anwendung eine Symbolleiste hinzu, die dem Benutzer ermöglicht, in und auszurichten, zu verschieben und das Diagramm als Bild zu speichern. Diese Symbolleiste wird am unteren Rand des Fensters hinzugefügt.

```python
    def add_toolbar(self):
        self.toolbar = NavigationToolbar2Wx(self.canvas)
        self.toolbar.Realize()
        self.sizer.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
```
