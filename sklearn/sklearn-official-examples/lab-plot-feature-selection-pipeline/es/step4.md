# Evaluar la Canalización

Ahora evaluaremos la canalización en el subconjunto de prueba utilizando el método `predict`. La canalización seleccionará las 3 características más informativas basadas en el valor F de ANOVA, y la función `LinearSVC` hará predicciones en las características seleccionadas.

```python
from sklearn.metrics import classification_report

y_pred = anova_svm.predict(X_test)
print(classification_report(y_test, y_pred))
```
