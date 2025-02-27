# Graficando los resultados del Experimento 2

Graficamos los resultados del segundo experimento utilizando la biblioteca `matplotlib`. Observamos resultados similares al del primer experimento: las métricas ajustadas para el azar se mantienen constantemente cerca de cero, mientras que otras métricas tienden a aumentar con etiquetaciones más detalladas. La V-medida media del etiquetado aleatorio aumenta significativamente a medida que el número de clusters se acerca al total de muestras utilizadas para calcular la medida.

```python
n_samples = 100
n_clusters_range = np.linspace(2, n_samples, 10).astype(int)

plt.figure(2)

plots = []
names = []

for marker, (score_name, score_func) in zip("d^vx.,", score_funcs):
    scores = uniform_labelings_scores(score_func, n_samples, n_clusters_range)
    plots.append(
        plt.errorbar(
            n_clusters_range,
            np.median(scores, axis=1),
            scores.std(axis=1),
            alpha=0.8,
            linewidth=2,
            marker=marker,
        )[0]
    )
    names.append(score_name)

plt.title(
    "Medidas de clustering para 2 etiquetados uniformes aleatorios\ncon igual número de clusters"
)
plt.xlabel(f"Número de clusters (El número de muestras está fijo en {n_samples})")
plt.ylabel("Valor de puntuación")
plt.legend(plots, names)
plt.ylim(bottom=-0.05, top=1.05)
plt.show()
```
