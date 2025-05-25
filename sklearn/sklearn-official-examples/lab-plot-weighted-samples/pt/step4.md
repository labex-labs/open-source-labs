# Treinar Modelos

Criaremos dois modelos SVM. O primeiro modelo não levará em consideração os pesos de amostra, e o segundo modelo levará em consideração os pesos de amostra que acabamos de criar.

```python
clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=sample_weight_last_ten)
```
