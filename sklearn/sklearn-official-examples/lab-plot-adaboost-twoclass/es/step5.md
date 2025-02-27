# Graficar las puntuaciones de decisión de dos clases

En este paso, graficaremos las puntuaciones de decisión de dos clases. Usaremos el método `decision_function` del clasificador AdaBoost para obtener las puntuaciones de decisión para cada muestra en el conjunto de datos. Luego graficaremos los histogramas de las puntuaciones de decisión para cada clase.

```python
# Graficar las puntuaciones de decisión de dos clases
twoclass_output = bdt.decision_function(X)
plot_range = (twoclass_output.min(), twoclass_output.max())
plt.subplot(122)
for i, n, c in zip(range(2), class_names, plot_colors):
    plt.hist(
        twoclass_output[y == i],
        bins=10,
        range=plot_range,
        facecolor=c,
        label="Class %s" % n,
        alpha=0.5,
        edgecolor="k",
    )
x1, x2, y1, y2 = plt.axis()
plt.axis((x1, x2, y1, y2 * 1.2))
plt.legend(loc="upper right")
plt.ylabel("Samples")
plt.xlabel("Score")
plt.title("Decision Scores")

plt.tight_layout()
plt.subplots_adjust(wspace=0.35)
plt.show()
```
