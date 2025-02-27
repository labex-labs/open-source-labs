# Ajustar el modelo sin pesos

Ajustamos un modelo sin pesos utilizando el algoritmo SGDClassifier de la biblioteca scikit-learn. Luego graficamos la función de decisión del modelo sin pesos.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
no_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["solid"])
```
