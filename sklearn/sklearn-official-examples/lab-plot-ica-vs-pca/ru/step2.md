# Использование алгоритма PCA

В этом шаге мы используем алгоритм PCA для нахождения ортогональных направлений в исходном пространстве признаков, которые соответствуют направлениям, обусловливающим максимальную дисперсию.

```python
pca = PCA()
S_pca_ = pca.fit(X).transform(X)
```
