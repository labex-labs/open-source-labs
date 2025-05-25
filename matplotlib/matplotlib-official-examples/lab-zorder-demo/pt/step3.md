# Definindo o Zorder para Ticks e Linhas de Grade

Podemos usar o método `set_axisbelow()` ou o parâmetro `axes.axisbelow` para definir o `zorder` de ticks (marcas) e linhas de grade.

```python
ax = plt.axes()
ax.plot([1, 2, 3], [2, 4, 3])
ax.set_axisbelow(True)
ax.yaxis.grid(color='gray', linestyle='dashed')
```
