# Graficando los resultados del Experimento 1

Graficamos los resultados del primer experimento utilizando las bibliotecas `matplotlib` y `seaborn`. El índice Rand se estabiliza para `n_clusters` > `n_classes`. Otras medidas no ajustadas, como la V-Measure, muestran una dependencia lineal entre el número de clusters y el número de muestras. Las medidas ajustadas para el azar, como el ARI y el AMI, presentan algunas variaciones aleatorias centradas en una puntuación media de 0.0, independientemente del número de muestras y clusters.

```python
import matplotlib.pyplot as plt
import seaborn as sns

n_samples = 1000
n_classes = 10
n_clusters_range = np.linspace(2, 100, 10).astype(int)
plots = []
names = []

sns.color_palette("colorblind")
plt.figure(1)

for marker, (score_name, score_func) in zip("d^vx.,", score_funcs):
    scores = fixed_classes_uniform_labelings_scores(
        score_func, n_samples, n_clusters_range, n_classes=n_classes
    )
    plots.append(
        plt.errorbar(
            n_clusters_range,
            scores.mean(axis=1),
            scores.std(axis=1),
            alpha=0.8,
            linewidth=1,
            marker=marker,
        )[0]
    )
    names.append(score_name)

plt.title(
    "Medidas de clustering para etiquetado uniforme aleatorio\n"
    f"en contra de la asignación de referencia con {n_classes} clases"
)
plt.xlabel(f"Número de clusters (El número de muestras está fijo en {n_samples})")
plt.ylabel("Valor de puntuación")
plt.ylim(bottom=-0.05, top=1.05)
plt.legend(plots, names, bbox_to_anchor=(0.5, 0.5))
plt.show()
```
