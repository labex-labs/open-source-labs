# Crear el gráfico de pastel

Ahora podemos crear el gráfico de pastel. Comenzamos definiendo los objetos de figura y eje:

```python
# crear figura y asignar objetos de eje
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(9, 5))
fig.subplots_adjust(wspace=0)
```

Luego establecemos los parámetros para el gráfico de pastel y lo trazamos:

```python
# rotar para que la primera porción se divida por el eje x
ángulo = -180 * overall_ratios[0]
wedges, *_ = ax1.pie(overall_ratios, autopct='%1.1f%%', startangle=ángulo,
                     labels=labels, explode=explode)
```
