# Entrenar modelos

Crearemos dos modelos de SVM. El primer modelo no tomará en cuenta los pesos de muestra, y el segundo modelo tomará en cuenta los pesos de muestra que acabamos de crear.

```python
clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=sample_weight_last_ten)
```
