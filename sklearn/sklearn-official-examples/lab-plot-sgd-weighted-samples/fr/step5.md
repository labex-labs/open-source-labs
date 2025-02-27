# Ajuster le modèle pondéré

Nous ajustons un modèle pondéré en utilisant le même algorithme que dans l'Étape 4, mais cette fois-ci, nous passons l'argument sample_weight à la méthode fit. Nous traçons ensuite la fonction de décision du modèle pondéré.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y, sample_weight=sample_weight)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
samples_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["dashed"])
```
