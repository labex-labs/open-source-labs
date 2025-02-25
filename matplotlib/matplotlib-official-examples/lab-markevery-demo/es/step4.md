# Crear gráficos con zoom

Creamos otro conjunto de subgráficos, esta vez para mostrar cómo se comporta `markevery` en gráficos con zoom. Notamos que la submuestreación basada en enteros selecciona puntos de los datos subyacentes y es independiente de la vista, mientras que la submuestreación basada en flotantes está relacionada con la diagonal de los ejes y cambia el rango de datos mostrado.

```python
# create zoomed plots
fig, axs = plt.subplots(3, 3, figsize=(10, 6), layout='constrained')
for ax, markevery in zip(axs.flat, cases):
    ax.set_title(f'markevery={markevery}')
    ax.plot(x, y, 'o', ls='-', ms=4, markevery=markevery)
    ax.set_xlim((6, 6.7))
    ax.set_ylim((1.1, 1.7))
```
