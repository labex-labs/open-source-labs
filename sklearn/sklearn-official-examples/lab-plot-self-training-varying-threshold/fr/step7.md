# Visualiser les résultats

```python
ax1 = plt.subplot(211)
ax1.errorbar(
    x_values, scores.mean(axis=1), yerr=scores.std(axis=1), capsize=2, color="b"
)
ax1.set_ylabel("Précision", color="b")
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
ax2.set_ylabel("Nombre d'échantillons étiquetés", color="g")
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
ax3.set_ylabel("Nombre d'itérations")
ax3.set_xlabel("Seuil")

plt.show()
```

Nous traçons les résultats de notre expérience à l'aide de Matplotlib. Le graphique supérieur montre le nombre d'échantillons étiquetés dont dispose le classifieur à la fin de l'ajustement, ainsi que la précision du classifieur. Le graphique inférieur montre la dernière itération au cours de laquelle un échantillon a été étiqueté.
