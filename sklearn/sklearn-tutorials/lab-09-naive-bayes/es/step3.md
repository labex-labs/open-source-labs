# Entrenar y evaluar el clasificador Naive Bayes Gaussiano

Ahora, entrenaremos el clasificador Naive Bayes Gaussiano en el conjunto de entrenamiento y evaluaremos su rendimiento en el conjunto de prueba. Usaremos la clase `GaussianNB` del módulo `sklearn.naive_bayes`.

```python
from sklearn.naive_bayes import GaussianNB

# Crear un clasificador Naive Bayes Gaussiano
gnb = GaussianNB()

# Entrenar el clasificador
gnb.fit(X_train, y_train)

# Predecir la variable objetivo para el conjunto de prueba
y_pred = gnb.predict(X_test)

# Calcular la precisión del clasificador
accuracy = (y_pred == y_test).sum() / len(y_test)
print("Precisión:", accuracy)
```
