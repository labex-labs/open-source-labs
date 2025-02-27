# Entraîner le modèle

Nous allons entraîner le modèle en utilisant la régression logistique avec une pénalité L1 et l'algorithme SAGA. Nous allons définir la valeur de `C` sur 50,0 divisée par le nombre d'échantillons d'entraînement.

```python
# Augmenter la tolérance pour une convergence plus rapide
clf = LogisticRegression(C=50.0 / train_samples, penalty="l1", solver="saga", tol=0.1)
clf.fit(X_train, y_train)
```
