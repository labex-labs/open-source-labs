# Crear el gráfico de barras

El siguiente paso es crear el gráfico de barras. Utilizaremos la función `bar()` para crear el gráfico. Crearemos dos conjuntos de barras, una para el té y otra para el café. También agregaremos barras de error al gráfico.

```python
ax.bar(ind, tea_means, width, bottom=0*cm, yerr=tea_std, label='Tea')
ax.bar(ind + width, coffee_means, width, bottom=0*cm, yerr=coffee_std,
       label='Coffee')
```
