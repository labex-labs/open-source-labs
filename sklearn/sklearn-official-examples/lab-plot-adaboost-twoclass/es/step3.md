# Crear y ajustar un árbol de decisión potenciado por AdaBoost

En este paso, crearemos un árbol de decisión potenciado por AdaBoost utilizando la clase `AdaBoostClassifier` del módulo `sklearn.ensemble`. Usaremos el árbol de decisión como estimador base y estableceremos el parámetro `max_depth` en 1. También estableceremos el parámetro `algorithm` en "SAMME" y el parámetro `n_estimators` en 200. Finalmente, ajustaremos el clasificador al conjunto de datos.

```python
bdt = AdaBoostClassifier(
    DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200
)

bdt.fit(X, y)
```
