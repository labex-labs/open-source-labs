# Негативные компоненты - NMF

Далее мы применяем разложение матрицы на неотрицательные слагаемые (Non - negative Matrix Factorization - NMF), которое разлагает матрицу данных на две неотрицательные матрицы, одну из которых содержит базисные векторы, а другая - коэффициенты. Это приводит к представлению данных в виде набора частей.

```python
# Non-negative components - NMF
nmf_estimator = decomposition.NMF(n_components=n_components, tol=5e-3)
nmf_estimator.fit(faces)  # original non- negative dataset
plot_gallery("Non-negative components - NMF", nmf_estimator.components_[:n_components])
```
