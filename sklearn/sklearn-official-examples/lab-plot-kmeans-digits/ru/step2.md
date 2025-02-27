# Определение бенчмарка оценки

Мы определим бенчмарк для сравнения различных методов инициализации для K-Means. Наш бенчмарк будет:

- создавать конвейер, который масштабирует данные с использованием `StandardScaler`
- обучать и замерять время настройки конвейера
- измерять производительность кластеризации, полученной с использованием различных метрик

```python
from time import time
from sklearn import metrics
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def bench_k_means(kmeans, name, data, labels):
    """Бенчмарк для оценки методов инициализации KMeans.

    Параметры
    ----------
    kmeans : экземпляр KMeans
        Экземпляр `KMeans` с уже установленной инициализацией.
    name : str
        Название стратегии. Будет использоваться для отображения результатов в таблице.
    data : ndarray формы (n_samples, n_features)
        Данные для кластеризации.
    labels : ndarray формы (n_samples,)
        Метки, используемые для вычисления метрик кластеризации, требующих некоторого контроля.
    """
    t0 = time()
    estimator = make_pipeline(StandardScaler(), kmeans).fit(data)
    fit_time = time() - t0
    results = [name, fit_time, estimator[-1].inertia_]

    # Определить метрики, которые требуют только истинных меток и меток оценщика
    clustering_metrics = [
        metrics.homogeneity_score,
        metrics.completeness_score,
        metrics.v_measure_score,
        metrics.adjusted_rand_score,
        metrics.adjusted_mutual_info_score,
    ]
    results += [m(labels, estimator[-1].labels_) for m in clustering_metrics]

    # Коэффициент силуэта требует полного набора данных
    results += [
        metrics.silhouette_score(
            data,
            estimator[-1].labels_,
            metric="euclidean",
            sample_size=300,
        )
    ]

    # Показать результаты
    formatter_result = (
        "{:9s}\t{:.3f}s\t{:.0f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}\t{:.3f}"
    )
    print(formatter_result.format(*results))
```
