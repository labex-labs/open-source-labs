# Crear un modelo de SVM con y sin desempate

En este paso, crearemos dos modelos de SVM: uno con el desempate deshabilitado y otro con el desempate habilitado. Utilizaremos la clase `SVC` de scikit-learn para crear estos modelos. El parámetro `break_ties` se establece en `False` y `True` para los dos modelos, respectivamente.

```python
for break_ties, title, ax in zip((False, True), titles, sub.flatten()):
    svm = SVC(
        kernel="linear", C=1, break_ties=break_ties, decision_function_shape="ovr"
    ).fit(X, y)
```
