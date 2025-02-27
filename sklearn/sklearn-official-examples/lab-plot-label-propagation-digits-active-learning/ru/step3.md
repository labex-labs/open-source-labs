# Обучение модели распространения меток

Теперь мы обучим модель распространения меток на помеченных точках данных и используем ее для предсказания меток оставшихся не помеченных точек данных.

```python
from sklearn.semi_supervised import LabelSpreading

lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
predicted_labels = lp_model.transduction_[unlabeled_indices]
```
