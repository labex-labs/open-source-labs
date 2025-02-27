# Graficar los resultados

Graficaremos los resultados de `GridSearchCV` utilizando un gráfico de barras. Esto nos permitirá comparar la precisión de diferentes técnicas de reducción de características.

```python
import pandas as pd

mean_scores = np.array(grid.cv_results_["mean_test_score"])
# las puntuaciones están en el orden de la iteración de param_grid, que es alfabética
mean_scores = mean_scores.reshape(len(C_OPTIONS), -1, len(N_FEATURES_OPTIONS))
# selecciona la puntuación para el mejor C
mean_scores = mean_scores.max(axis=0)
# crea un dataframe para facilitar la graficación
mean_scores = pd.DataFrame(
    mean_scores.T, index=N_FEATURES_OPTIONS, columns=etiquetas_reductor
)

ax = mean_scores.plot.bar()
ax.set_title("Comparando técnicas de reducción de características")
ax.set_xlabel("Número reducido de características")
ax.set_ylabel("Precisión de clasificación de dígitos")
ax.set_ylim((0, 1))
ax.legend(loc="upper left")

plt.show()
```
