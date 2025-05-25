# Definir o Padrão de Avaliação

Definiremos um padrão para comparar diferentes métodos de inicialização para K-Means. O nosso padrão:

- criará um pipeline que escalará os dados usando um `StandardScaler`;
- treinará e cronometrará o ajuste do pipeline;
- medirá o desempenho do agrupamento obtido através de diferentes métricas.

```python
from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def bench_k_means(kmeans, name, data, labels):
    """Benchmark para avaliar os métodos de inicialização KMeans.

    Parâmetros
    ----------
    kmeans : Instância KMeans
        Uma instância `KMeans` com a inicialização já definida.
    name : str
        Nome atribuído à estratégia. Será usado para mostrar os resultados numa tabela.
    data : ndarray de forma (n_samples, n_features)
        Os dados a agrupar.
    labels : ndarray de forma (n_samples,)
        As etiquetas usadas para calcular as métricas de agrupamento que requerem alguma supervisão.
    """
    t0 = time()
    estimator = make_pipeline(StandardScaler(), kmeans).fit(data)
    fit_time = time() - t0
    results = [name, fit_time, estimator[-1].inertia_]

    # Defina as métricas que requerem apenas as etiquetas verdadeiras e as etiquetas do estimador
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    results += [m(labels, estimator[-1].labels_) for m in clustering_metrics]

    # A pontuação de silhueta requer todo o conjunto de dados
    results += [
        metrics.silhouette_score(
            data,
            estimator[-1].labels_,
            metric="euclidean",
            sample_size=300,
        )
    ]

    # Mostrar os resultados
    formatter_result = (
        "{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}"
    )
    print(formatter_result.format(*results))
```
