# Visualizar resultados

```python
ax1 = plt.subplot(211)
ax1.errorbar(
    x_values, scores.mean(axis=1), yerr=scores.std(axis=1), capsize=2, color="b"
)
ax1.set_ylabel("Precisión", color="b")
ax1.tick_params("y", colors="b")

ax2 = ax1.twinx()
ax2.errorbar(
    x_values,
    amount_labeled.mean(axis=1),
    yerr=amount_labeled.std(axis=1),
    capsize=2,
    color="g",
)
ax2.set_ylim(bottom=0)
ax2.set_ylabel("Cantidad de muestras etiquetadas", color="g")
ax2.tick_params("y", colors="g")

ax3 = plt.subplot(212, sharex=ax1)
ax3.errorbar(
    x_values,
    amount_iterations.mean(axis=1),
    yerr=amount_iterations.std(axis=1),
    capsize=2,
    color="b",
)
ax3.set_ylim(bottom=0)
ax3.set_ylabel("Cantidad de iteraciones")
ax3.set_xlabel("Umbral")

plt.show()
```

Graficamos los resultados de nuestro experimento utilizando Matplotlib. La gráfica superior muestra la cantidad de muestras etiquetadas que tiene disponible el clasificador al final del ajuste, y la precisión del clasificador. La gráfica inferior muestra la última iteración en la que se etiquetó una muestra.
