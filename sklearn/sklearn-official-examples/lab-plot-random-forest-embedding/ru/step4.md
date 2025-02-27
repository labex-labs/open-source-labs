# Визуализация результата после понижения размерности с использованием Truncated SVD

В этом шаге мы визуализируем результат после понижения размерности с использованием Truncated SVD.

```python
svd = TruncatedSVD(n_components=2)
X_reduced = svd.fit_transform(X_transformed)
```
