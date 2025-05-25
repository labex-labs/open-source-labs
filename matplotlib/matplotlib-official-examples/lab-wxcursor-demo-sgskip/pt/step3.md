# Atualizar a Barra de Status

Finalmente, definiremos um método para atualizar a barra de status com a localização do cursor sempre que o mouse se mover sobre o gráfico.

```python
def UpdateStatusBar(self, event):
    if event.inaxes:
        self.statusBar.SetStatusText(f"x={event.xdata}  y={event.ydata}")
```
