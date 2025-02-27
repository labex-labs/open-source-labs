# Ajustar un clasificador de ensamble (Bagging)

Ahora, ajustaremos un clasificador de ensamble (Bagging) a los datos de entrenamiento. El clasificador de ensamble (Bagging) es un método de ensamble que utiliza muestreo con remuestreo (bootstrap) para crear múltiples modelos base (a menudo árboles de decisión) y agrega sus predicciones mediante votación mayoritaria.

```python
bagging = BaggingClassifier(DecisionTreeClassifier(), n_estimators=10)
bagging.fit(X_train, y_train)
```
