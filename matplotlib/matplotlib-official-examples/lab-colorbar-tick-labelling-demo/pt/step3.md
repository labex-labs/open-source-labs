# Personalizar os rótulos dos ticks na barra de cores vertical

Em seguida, personalizaremos os rótulos dos ticks na barra de cores vertical. Criaremos uma barra de cores usando `colorbar` e especificaremos as localizações dos ticks usando o parâmetro `ticks`. Em seguida, definiremos os rótulos dos ticks usando `set_yticklabels` no atributo `ax` do objeto da barra de cores.

```python
# Add colorbar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[-1, 0, 1])
cbar.ax.set_yticklabels(['< -1', '0', '> 1'])  # vertically oriented colorbar
```
