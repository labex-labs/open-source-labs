# Crear gráficos con escalas lineales

A continuación, creamos un conjunto de subgráficos para mostrar cómo se comporta `markevery` con escalas lineales. Iteramos a través de la lista `cases` y graficamos cada caso en un subgráfico separado. Usamos el parámetro `markevery` para especificar qué puntos de datos marcar.

```python
# create plots with linear scales
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
```
