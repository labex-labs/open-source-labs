# Эйгенлица - PCA с использованием случайного разложения сингулярных значений

Первым методом, который мы применяем, является PCA (Principal Component Analysis - анализ главных компонент), который представляет собой линейный метод снижения размерности, использующий разложение сингулярных значений (SVD - Singular Value Decomposition) данных для проекции их в пространство с меньшей размерностью. Мы используем случайное разложение сингулярных значений, которое представляет собой более быстрый приближенный алгоритм по сравнению с стандартным алгоритмом SVD. Мы строим первые шесть главных компонент, которые называются эйгенлицами.

```python
# Eigenfaces - PCA using randomized SVD
pca_estimator = decomposition.PCA(
    n_components=n_components, svd_solver="randomized", whiten=True
)
pca_estimator.fit(faces_centered)
plot_gallery(
    "Eigenfaces - PCA using randomized SVD", pca_estimator.components_[:n_components]
)
```
