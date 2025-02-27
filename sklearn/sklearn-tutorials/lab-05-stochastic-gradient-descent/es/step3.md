# Entrenar un clasificador utilizando SGD

Ahora entrenaremos un clasificador utilizando la clase SGDClassifier. Utilizaremos la función de pérdida log_loss y la penalización l2.

```python
# Entrenar un clasificador utilizando SGD
clf = SGDClassifier(loss="log_loss", penalty="l2", max_iter=100, random_state=42)
clf.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
y_pred = clf.predict(X_test)

# Medir la precisión del clasificador
accuracy = accuracy_score(y_test, y_pred)

# Imprimir la precisión
print("Precisión del clasificador:", accuracy)
```
