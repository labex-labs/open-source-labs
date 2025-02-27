# Entraînement des modèles

Nous allons créer deux modèles SVM. Le premier modèle ne prendra pas en compte les poids d'échantillonnage, et le second modèle prendra en compte les poids d'échantillonnage que nous venons de créer.

```python
clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=sample_weight_last_ten)
```
