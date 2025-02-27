# Обучение модели дерева решений на дискретизированном наборе данных

В этом шаге мы обучим модель дерева решений на дискретизированном наборе данных.

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X_binned, y)
```
