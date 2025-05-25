# Definir a posição do rótulo da barra de cores (colorbar)

Podemos definir a posição do rótulo da barra de cores usando o método `colorbar` e o método `set_label`. Podemos definir a posição como `'top'`, `'bottom'`, `'left'` ou `'right'`. Neste exemplo, definiremos a posição como `'top'`.

```python
cbar = fig.colorbar(sc)
cbar.set_label("ZLabel", loc='top')
```
