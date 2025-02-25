# Обновите статусную строку

Наконец, мы определим метод для обновления статусной строки координатами курсора при перемещении мыши по графику.

```python
def UpdateStatusBar(self, event):
    if event.inaxes:
        self.statusBar.SetStatusText(f"x={event.xdata}  y={event.ydata}")
```
