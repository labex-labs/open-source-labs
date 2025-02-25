# Crear el gráfico de barras

A continuación, creamos el gráfico de barras apiladas. Comenzamos definiendo los parámetros del gráfico:

```python
# parámetros del gráfico de barras
bottom = 1
width =.2

# Agregar desde la parte superior coincide con la leyenda.
for j, (height, label) in enumerate(reversed([*zip(age_ratios, age_labels)])):
    bottom -= height
    bc = ax2.bar(0, height, width, bottom=bottom, color='C0', label=label,
                 alpha=0.1 + 0.25 * j)
    ax2.bar_label(bc, labels=[f"{height:.0%}"], label_type='center')
```
