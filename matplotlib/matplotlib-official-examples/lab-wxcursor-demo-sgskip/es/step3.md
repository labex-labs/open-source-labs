# Actualizar la barra de estado

Finalmente, definiremos un método para actualizar la barra de estado con la ubicación del cursor cada vez que el mouse se mueva sobre el trazado.

```python
def UpdateStatusBar(self, event):
    if event.inaxes:
        self.statusBar.SetStatusText(f"x={event.xdata}  y={event.ydata}")
```
