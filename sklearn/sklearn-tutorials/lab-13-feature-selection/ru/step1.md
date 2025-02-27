# Удаление признаков с низкой дисперсией

В scikit-learn класс `VarianceThreshold` можно использовать для удаления признаков с низкой дисперсией. Признаки с низкой дисперсией обычно не дают много информации для модели. Мы покажем, как использовать `VarianceThreshold` для удаления признаков с нулевой дисперсией.

```python
from sklearn.feature_selection import VarianceThreshold

X = [[0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 1], [0, 1, 0], [0, 1, 1]]

# Initialize VarianceThreshold with a threshold of 80% variability
sel = VarianceThreshold(threshold=(.8 * (1 -.8)))

# Select features with high variability
X_selected = sel.fit_transform(X)

print("Original X shape:", X.shape)
print("X with selected features shape:", X_selected.shape)
print("Selected features:", sel.get_support(indices=True))
```

Этот код демонстрирует, как использовать `VarianceThreshold` для удаления признаков с нулевой дисперсией из набора данных. Вывод покажет исходную форму набора данных и форму после выбора признаков с высокой дисперсией.
