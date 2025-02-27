# Обучение модели распространения меток (Label Spreading)

Мы обучаем модель распространения меток (Label Spreading) с параметрами gamma=0.25 и max_iter=20.

```python
lp_model = LabelSpreading(gamma=0.25, max_iter=20)
lp_model.fit(X, y_train)
```
