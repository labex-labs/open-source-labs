# Crear el modelo

En este paso, crearemos el modelo SVM-Kernel con tres kernels diferentes: lineal, polinomial y función de base radial (RBF). El kernel lineal se utiliza para puntos de datos linealmente separables, mientras que los kernels polinomial y RBF son útiles para puntos de datos no linealmente separables.

```python
# ajustar el modelo
for kernel in ("linear", "poly", "rbf"):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)
```
