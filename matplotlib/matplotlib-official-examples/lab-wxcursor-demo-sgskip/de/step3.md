# Aktualisieren der Statuszeile

Schließlich werden wir eine Methode definieren, um die Statuszeile mit der Cursor-Position zu aktualisieren, wenn sich die Maus über dem Diagramm bewegt.

```python
def UpdateStatusBar(self, event):
    if event.inaxes:
        self.statusBar.SetStatusText(f"x={event.xdata}  y={event.ydata}")
```
