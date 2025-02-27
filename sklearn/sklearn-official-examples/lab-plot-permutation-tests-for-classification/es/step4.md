# Representar los resultados

Representamos un histograma de las puntuaciones de permutación (la distribución nula) tanto para el conjunto de datos iris original como para los datos aleatorizados. También indicamos la puntuación obtenida por el clasificador en los datos originales utilizando una línea roja. El valor p se muestra en cada gráfico.

```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots()

# Datos originales
ax.hist(perm_scores_iris, bins=20, densidad=True)
ax.axvline(score_iris, ls="--", color="r")
etiqueta_puntuación = f"Puntuación en datos originales:\n{score_iris:.2f}\n(p-valor: {pvalue_iris:.3f})"
ax.text(0.7, 10, etiqueta_puntuación, tamaño_fuente=12)
ax.set_xlabel("Puntuación de exactitud")
_ = ax.set_ylabel("Densidad de probabilidad")

plt.show()

fig, ax = plt.subplots()

# Datos aleatorios
ax.hist(perm_scores_rand, bins=20, densidad=True)
ax.set_xlim(0.13)
ax.axvline(score_rand, ls="--", color="r")
etiqueta_puntuación = f"Puntuación en datos originales:\n{score_rand:.2f}\n(p-valor: {pvalue_rand:.3f})"
ax.text(0.14, 7.5, etiqueta_puntuación, tamaño_fuente=12)
ax.set_xlabel("Puntuación de exactitud")
ax.set_ylabel("Densidad de probabilidad")

plt.show()
```

注：这里代码中的`densidad`是对`density`不太准确的翻译，实际使用中建议保留`density`英文原文；`tamaño_fuente`是对`fontsize`不太准确的翻译，实际使用中建议保留`fontsize`英文原文 。
