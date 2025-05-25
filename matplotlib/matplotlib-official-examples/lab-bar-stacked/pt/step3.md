# Criar um Gráfico de Barras Empilhadas

Criaremos um gráfico de barras empilhadas usando `matplotlib.pyplot.bar` e iteraremos por cada categoria de peso para empilhar as barras.

```python
fig, ax = plt.subplots()
bottom = np.zeros(3)

for boolean, weight_count in weight_counts.items():
    p = ax.bar(species, weight_count, width, label=boolean, bottom=bottom)
    bottom += weight_count

ax.set_title("Número de pinguins com massa corporal acima da média")
ax.legend(loc="upper right")
```
