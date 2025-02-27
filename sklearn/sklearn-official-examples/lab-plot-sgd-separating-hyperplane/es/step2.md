# Entrenar el modelo de SVM con SGD

A continuación, necesitamos entrenar el modelo de SVM utilizando SGD. Utilizaremos la clase `SGDClassifier` de Scikit-learn para entrenar el modelo. Estableceremos el parámetro `loss` en "hinge" para utilizar el algoritmo de SVM y el parámetro `alpha` en 0.01 para controlar la fuerza de regularización. También estableceremos el parámetro `max_iter` en 200 para limitar el número de iteraciones.

```python
# ajustar el modelo
clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)
clf.fit(X, Y)
```
