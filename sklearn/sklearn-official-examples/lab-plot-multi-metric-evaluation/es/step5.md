# Visualizar los resultados

En este paso, visualizaremos los resultados de la búsqueda en cuadrícula utilizando un gráfico. Graficaremos las puntuaciones AUC y Precisión para ambos conjuntos de entrenamiento y prueba.

```python
plt.figure(figsize=(13, 13))
plt.title("GridSearchCV evaluando utilizando múltiples clasificadores simultáneamente", fontsize=16)

plt.xlabel("min_samples_split")
plt.ylabel("Puntuación")

ax = plt.gca()
ax.set_xlim(0, 402)
ax.set_ylim(0.73, 1)

# Obtener la matriz numpy regular a partir de la MaskedArray
X_axis = np.array(results["param_min_samples_split"].data, dtype=float)

for scorer, color in zip(sorted(scoring), ["g", "k"]):
    for sample, style in (("train", "--"), ("test", "-")):
        sample_score_mean = results["mean_%s_%s" % (sample, scorer)]
        sample_score_std = results["std_%s_%s" % (sample, scorer)]
        ax.fill_between(
            X_axis,
            sample_score_mean - sample_score_std,
            sample_score_mean + sample_score_std,
            alpha=0.1 if sample == "test" else 0,
            color=color,
        )
        ax.plot(
            X_axis,
            sample_score_mean,
            style,
            color=color,
            alpha=1 if sample == "test" else 0.7,
            label="%s (%s)" % (scorer, sample),
        )

    best_index = np.nonzero(results["rank_test_%s" % scorer] == 1)[0][0]
    best_score = results["mean_test_%s" % scorer][best_index]

    # Graficar una línea vertical discontinua en la mejor puntuación para ese clasificador marcada por x
    ax.plot(
        [
            X_axis[best_index],
        ]
        * 2,
        [0, best_score],
        linestyle="-.",
        color=color,
        marker="x",
        markeredgewidth=3,
        ms=8,
    )

    # Anotar la mejor puntuación para ese clasificador
    ax.annotate("%0.2f" % best_score, (X_axis[best_index], best_score + 0.005))

plt.legend(loc="best")
plt.grid(False)
plt.show()
```
