# Выбор признаков с использованием последовательного отбора признаков

Мы используем последовательный селектор признаков (Sequential Feature Selector, SFS) для выбора признаков. SFS - это жадный алгоритм, при котором на каждой итерации мы выбираем наилучший новый признак для добавления к нашим выбранным признакам на основе оценки кросс - валидации. Также мы можем идти в обратном направлении (обратный SFS), то есть начинать с всех признаков и жадно выбирать признаки для удаления по одному.

```python
from sklearn.feature_selection import SequentialFeatureSelector

sfs_forward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="forward").fit(X, y)
sfs_backward = SequentialFeatureSelector(ridge, n_features_to_select=2, direction="backward").fit(X, y)

print(f"Features selected by forward sequential selection: {feature_names[sfs_forward.get_support()]}")
print(f"Features selected by backward sequential selection: {feature_names[sfs_backward.get_support()]}")
```
