# Criar Gráfico de Barras Empilhadas Verticais

Criaremos um gráfico de barras empilhadas verticais usando a função `plt.bar` para representar a perda incorrida por diferentes desastres naturais ao longo dos anos. Usaremos um loop `for` para iterar sobre cada linha de dados e plotar as barras.

```python
n_rows = len(data)

index = np.arange(len(columns)) + 0.3
bar_width = 0.4

y_offset = np.zeros(len(columns))

cell_text = []
for row in range(n_rows):
    plt.bar(index, data[row], bar_width, bottom=y_offset, color=colors[row])
    y_offset = y_offset + data[row]
    cell_text.append(['%1.1f' % (x / 1000.0) for x in y_offset])
```
