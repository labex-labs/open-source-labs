# Mejorando el modelo

Si la precisión de nuestro modelo no es satisfactoria, podemos intentar mejorarlo ajustando los hiperparámetros del algoritmo SVM. Por ejemplo, podemos intentar cambiar el valor del parámetro `C`:

```python
# Crea el clasificador SVM con un valor diferente de C
clf = SVC(kernel='linear', C=0.1)

# Entrena el clasificador con los datos de entrenamiento
clf.fit(X_train, y_train)

# Predecir las etiquetas del conjunto de prueba
y_pred = clf.predict(X_test)

# Calcular la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)

# Imprimir la precisión del modelo
print("Precisión:", accuracy)
```
