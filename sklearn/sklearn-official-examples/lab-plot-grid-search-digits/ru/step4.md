# Обучение модели и предсказание

Мы обучим модель и сделаем предсказания на наборе для оценки.

```python
grid_search.fit(X_train, y_train)

# The parameters selected by the grid-search with our custom strategy are:
grid_search.best_params_

# Finally, we evaluate the fine-tuned model on the left-out evaluation set: the
# `grid_search` object **has automatically been refit** on the full training
# set with the parameters selected by our custom refit strategy.
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))
```
