# Entrenar y evaluar el modelo

Ahora, entrenemos un clasificador de máquinas de vectores de soporte (SVM) en el conjunto de entrenamiento y evaluemos su rendimiento en el conjunto de prueba.

```python
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Accuracy: ", score)
```
