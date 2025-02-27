# Загрузка и подготовка набора данных

Загружаем набор данных цифр и готовим его для кластеризации, извлекая данные и метки целей. Также устанавливаем случайный种子 в ноль, чтобы обеспечить воспроизводимость.

```python
digits = datasets.load_digits()
X, y = digits.data, digits.target
n_samples, n_features = X.shape
np.random.seed(0)
```
