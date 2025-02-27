# Representar los resultados

El último paso es representar los resultados. Utilizaremos dos subgráficos para representar las puntuaciones de entrenamiento y prueba, y el número de iteraciones y el tiempo de ajuste. Utilizaremos diferentes estilos de línea para cada estimador y criterio de parada.

```python
# Definir lo que se va a representar
lines = "Criterio de parada"
x_axis = "max_iter"
styles = ["-.", "--", "-"]

# Primera representación: puntuaciones de entrenamiento y prueba
fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 4))
for ax, y_axis in zip(axes, ["Puntuación de entrenamiento", "Puntuación de prueba"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

# Segunda representación: n_iter y tiempo de ajuste
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
for ax, y_axis in zip(axes, ["n_iter_", "Tiempo de ajuste (seg)"]):
    for style, (criterion, group_df) in zip(styles, results_df.groupby(lines)):
        group_df.plot(x=x_axis, y=y_axis, label=criterion, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

plt.show()
```
