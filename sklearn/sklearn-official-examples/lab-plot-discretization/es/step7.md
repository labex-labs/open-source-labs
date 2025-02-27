# Entrenar un modelo de árbol de decisión

En este paso, entrenaremos un modelo de árbol de decisión en el conjunto de datos original.

```python
reg = DecisionTreeRegressor(min_samples_split=3, random_state=0).fit(X, y)
```
