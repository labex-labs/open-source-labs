# Evaluación

En este paso, evaluamos el rendimiento del modelo en el conjunto de datos de prueba. Utilizamos la función `classification_report` del módulo `sklearn.metrics` para generar el informe de clasificación tanto para el modelo de tubo como para el modelo de regresión logística.

```python
from sklearn import metrics

Y_pred = rbm_features_classifier.predict(X_test)
print(
    "Regresión logística utilizando características de RBM:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)

# Entrenando el clasificador de regresión logística directamente en los píxeles
raw_pixel_classifier = clone(logistic)
raw_pixel_classifier.C = 100.0
raw_pixel_classifier.fit(X_train, Y_train)

Y_pred = raw_pixel_classifier.predict(X_test)
print(
    "Regresión logística utilizando características de píxeles brutos:\n%s\n"
    % (metrics.classification_report(Y_test, Y_pred))
)
```
