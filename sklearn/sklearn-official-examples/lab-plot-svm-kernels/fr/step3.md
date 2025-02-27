# Création du modèle

Dans cette étape, nous allons créer le modèle SVM-Kernel avec trois noyaux différents : linéaire, polynôme et fonction de base radiale (RBF). Le noyau linéaire est utilisé pour les points de données linéairement séparables, tandis que les noyaux polynôme et RBF sont utiles pour les points de données non linéairement séparables.

```python
# fit the model
for kernel in ("linear", "poly", "rbf"):
    clf = svm.SVC(kernel=kernel, gamma=2)
    clf.fit(X, Y)
```
