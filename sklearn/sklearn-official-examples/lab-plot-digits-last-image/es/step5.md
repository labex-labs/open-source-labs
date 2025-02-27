# Evaluando el modelo

Para evaluar el rendimiento de nuestro modelo, podemos utilizar la función `accuracy_score` de scikit-learn:

```python
from sklearn.metrics import accuracy_score

# Predecir las etiquetas del conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)

# Imprimir la precisión del modelo
print("Precisión:", accuracy)
```
