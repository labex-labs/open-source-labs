# Ajustar el modelo y hacer predicciones

Ajustaremos el modelo y haremos predicciones en el conjunto de evaluación.

```python
grid_search.fit(X_train, y_train)

# Los parámetros seleccionados por la búsqueda en cuadrícula con nuestra estrategia personalizada son:
grid_search.best_params_

# Finalmente, evaluamos el modelo ajustado en el conjunto de evaluación no utilizado: el
# objeto `grid_search` **ha sido automáticamente ajustado** en el conjunto de entrenamiento
# completo con los parámetros seleccionados por nuestra estrategia de ajuste personalizada.
y_pred = grid_search.predict(X_test)
print(classification_report(y_test, y_pred))
```
