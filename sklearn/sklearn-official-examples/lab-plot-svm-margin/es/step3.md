# Ajustar el modelo

Ajustamos el modelo SVM utilizando la clase `SVC` de scikit-learn. Establecemos el kernel en lineal y el parámetro de penalización `C` en 1 para el caso no regularizado y en 0,05 para el caso regularizado. Luego calculamos el hiperplano separador utilizando los coeficientes y el intercepto del modelo.

```python
for name, penalty in (("unreg", 1), ("reg", 0.05)):
    clf = svm.SVC(kernel="linear", C=penalty)
    clf.fit(X, Y)

    w = clf.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(-5, 5)
    yy = a * xx - (clf.intercept_[0]) / w[1]
```
