# Definir la referencia de evaluación

Definiremos una referencia para comparar diferentes métodos de inicialización para K-Means. Nuestra referencia:

- creará una tubería que escalará los datos utilizando un `StandardScaler`
- entrenará y medirá el tiempo de ajuste de la tubería
- medirá el rendimiento del agrupamiento obtenido a través de diferentes métricas

```python
from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def bench_k_means(kmeans, name, data, labels):
    """Referencia para evaluar los métodos de inicialización de KMeans.

    Parámetros
    ----------
    kmeans : instancia de KMeans
        Una instancia de `KMeans` con la inicialización ya establecida.
    name : str
        Nombre dado a la estrategia. Se utilizará para mostrar los resultados en una tabla.
    data : ndarray de forma (n_muestras, n_características)
        Los datos a agrupar.
    labels : ndarray de forma (n_muestras,)
        Las etiquetas utilizadas para calcular las métricas de agrupamiento que requieren alguna supervisión.
    """
    t0 = time()
    estimator = make_pipeline(StandardScaler(), kmeans).fit(data)
    fit_time = time() - t0
    results = [name, fit_time, estimator[-1].inertia_]

    # Definir las métricas que solo requieren las etiquetas reales y las etiquetas del estimador
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    results += [m(labels, estimator[-1].labels_) for m in clustering_metrics]

    # La puntuación de silueta requiere el conjunto de datos completo
    results += [
        metrics.silhouette_score(
            data,
            estimator[-1].labels_,
            metric="euclidean",
            sample_size=300,
        )
    ]

    # Mostrar los resultados
    formatter_result = (
        "{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}"
    )
    print(formatter_result.format(*results))
```
