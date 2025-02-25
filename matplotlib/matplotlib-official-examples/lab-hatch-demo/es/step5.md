# Crear un gráfico con parches sombreados

También puedes usar el sombreado con parches en tu gráfico. En este caso, usaremos la función `fill_between` para crear un parche sombreado.

```python
x = np.arange(0, 40, 0.2)
plt.fill_between(x, np.sin(x) * 4 + 30, y2=0, hatch='///', zorder=2, fc='c')
```
