# Ajustar el modelo con pesos

Ajustamos un modelo con pesos utilizando el mismo algoritmo que en el Paso 4, pero esta vez pasamos el argumento sample_weight al método fit. Luego graficamos la función de decisión del modelo con pesos.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y, sample_weight=sample_weight)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
samples_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["dashed"])
```
