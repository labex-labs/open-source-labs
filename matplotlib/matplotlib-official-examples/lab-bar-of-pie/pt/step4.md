# Criar o gráfico de barras

Em seguida, criamos o gráfico de barras empilhadas. Começamos definindo os parâmetros para o gráfico:

```python
# bar chart parameters
bottom = 1
width = .2

# Adding from the top matches the legend.
for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                 alpha=0.1 + 0.25 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')
```
