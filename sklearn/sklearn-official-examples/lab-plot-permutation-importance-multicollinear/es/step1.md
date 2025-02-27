# Entrenar un clasificador de bosque aleatorio

Primero cargamos el conjunto de datos de cáncer de mama de Wisconsin y lo dividimos en conjuntos de entrenamiento y prueba. Luego entrenamos un clasificador de bosque aleatorio en el conjunto de entrenamiento y evaluamos su precisión en el conjunto de prueba.

```python
data = load_breast_cancer()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
print("Precisión en los datos de prueba: {:.2f}".format(clf.score(X_test, y_test)))
```
