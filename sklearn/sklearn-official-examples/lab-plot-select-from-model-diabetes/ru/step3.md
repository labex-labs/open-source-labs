# Выбор признаков на основе важности

Мы выбираем два наиболее важных признака в соответствии с коэффициентами, используя `SelectFromModel`. `SelectFromModel` принимает параметр `threshold` и будет выбирать признаки, важность которых (определяемая коэффициентами) выше этого порога.

```python
from sklearn.feature_selection import SelectFromModel

threshold = np.sort(importance)[-3] + 0.01

sfm = SelectFromModel(ridge, threshold=threshold).fit(X, y)
print(f"Features selected by SelectFromModel: {feature_names[sfm.get_support()]}")
```
