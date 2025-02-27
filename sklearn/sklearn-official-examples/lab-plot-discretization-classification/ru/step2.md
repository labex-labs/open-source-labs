# Подготовка данных

В этом шаге мы подготовим синтетические наборы данных для классификации для дискретизации признаков. Мы будем использовать библиотеку scikit - learn для генерации трех разных наборов данных: moons,同心圆 (concentric circles) и линейно разделимые данные.

```python
h = 0.02  # step size in the mesh

n_samples = 100
datasets = [
    make_moons(n_samples=n_samples, noise=0.2, random_state=0),
    make_circles(n_samples=n_samples, noise=0.2, factor=0.5, random_state=1),
    make_classification(
        n_samples=n_samples,
        n_features=2,
        n_redundant=0,
        n_informative=2,
        random_state=2,
        n_clusters_per_class=1,
    ),
]
```
