# Entrenar y probar el clasificador de Regresión Logística

Ahora entrenaremos un clasificador de Regresión Logística utilizando la función `LogisticRegression` de scikit-learn y lo probaremos en el conjunto de prueba. Luego imprimiremos la puntuación de precisión del clasificador.

```python
from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression(max_iter=1000)
logistic.fit(X_train, y_train)
logistic_score = logistic.score(X_test, y_test)

print("Logistic Regression score: %f" % logistic_score)
```
