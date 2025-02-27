# Crear un modelo de SVM

Crearemos un modelo de SVM lineal con entrenamiento por SGD.

```python
# crear el modelo de SVM con entrenamiento por SGD
clf = SGDClassifier(loss="hinge", penalty="elasticnet", fit_intercept=True)
```
