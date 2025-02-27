# Настройка моделей ICA и PCA

Мы будем использовать FastICA для оценки независимых источников. Затем вычислим PCA для сравнения.

```python
from sklearn.decomposition import FastICA, PCA

# Вычислить ICA
ica = FastICA(n_components=3, whiten="arbitrary-variance")
S_ = ica.fit_transform(X)  # Восстановить сигналы
A_ = ica.mixing_  # Получить оцененную матрицу смешивания

# Мы можем "доказать", что модель ICA применима, выполнив обратное смешивание.
assert np.allclose(X, np.dot(S_, A_.T) + ica.mean_)

# Для сравнения вычислить PCA
pca = PCA(n_components=3)
H = pca.fit_transform(X)  # Восстановить сигналы на основе ортогональных компонентов
```
