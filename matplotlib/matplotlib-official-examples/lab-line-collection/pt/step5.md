# Mapear Cores para Valores

Também podemos mapear um array de valores para cores usando a função `ScalarMappable.set_array`. Criaremos um novo conjunto de dados e um novo objeto `LineCollection` com o parâmetro `array` definido para os valores `x`. Podemos então usar o método `colorbar` do objeto `Figure` para adicionar uma barra de cores ao gráfico.

```python
N = 50
x = np.arange(N)
ys = [x + i for i in x]
segs = [np.column_stack([x, y]) for y in ys]

fig, ax = plt.subplots()
ax.set_xlim(np.min(x), np.max(x))
ax.set_ylim(np.min(ys), np.max(ys))

line_segments = LineCollection(segs, array=x,
                               linewidths=(0.5, 1, 1.5, 2),
                               linestyles='solid')
ax.add_collection(line_segments)
axcb = fig.colorbar(line_segments)
axcb.set_label('Line Number')
ax.set_title('Line Collection with mapped colors')
plt.sci(line_segments)
plt.show()
```
