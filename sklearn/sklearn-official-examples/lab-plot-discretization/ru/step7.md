# Обучение модели дерева решений

В этом шаге мы обучим модель дерева решений на исходном наборе данных.

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X, y)
```
