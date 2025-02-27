# Entrenar el modelo

Entrenaremos un clasificador de máquinas de vectores de soporte (SVM) con un kernel lineal. Usaremos un parámetro de regularización C demasiado bajo para ver el impacto en los resultados.

```python
classifier = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)
```
