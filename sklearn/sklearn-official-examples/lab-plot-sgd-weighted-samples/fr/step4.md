# Ajuster le modèle non pondéré

Nous ajustons un modèle non pondéré à l'aide de l'algorithme SGDClassifier de la bibliothèque scikit-learn. Nous traçons ensuite la fonction de décision du modèle non pondéré.

```python
clf = linear_model.SGDClassifier(alpha=0.01, max_iter=100)
clf.fit(X, y)
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
no_weights = ax.contour(xx, yy, Z, levels=[0], linestyles=["solid"])
```
