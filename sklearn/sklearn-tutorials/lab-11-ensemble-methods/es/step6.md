# Ajustar un clasificador de bosque aleatorio

A continuación, ajustaremos un clasificador de bosque aleatorio a los datos de entrenamiento. El clasificador de bosque aleatorio también es un método de ensamble que utiliza muestreo con remuestreo (bootstrap) para crear múltiples árboles de decisión, pero también agrega aleatoriedad adicional al considerar solo un subconjunto de características en cada división.

```python
random_forest = RandomForestClassifier(n_estimators=10)
random_forest.fit(X_train, y_train)
```
