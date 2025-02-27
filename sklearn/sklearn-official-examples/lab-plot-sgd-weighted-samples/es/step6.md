# Agregar leyenda y mostrar la gráfica

Agregamos una leyenda a la gráfica para diferenciar entre los modelos sin pesos y con pesos. Luego mostramos la gráfica.

```python
no_weights_handles, _ = no_weights.legend_elements()
weights_handles, _ = samples_weights.legend_elements()
ax.legend(
    [no_weights_handles[0], weights_handles[0]],
    ["no weights", "with weights"],
    loc="lower left",
)

ax.set(xticks=(), yticks=())
plt.show()
```
