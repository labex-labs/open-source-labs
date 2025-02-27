# Ajuster le modèle avec des classes pondérées

Nous allons ajuster le modèle et obtenir l'hyperplan de séparation à l'aide de la fonction `SVC` de la bibliothèque `svm`. Nous utiliserons un noyau linéaire et définirons `class_weight` sur `{1: 10}`. Cela donnera plus de poids à la classe la plus petite.

```python
wclf = svm.SVC(kernel="linear", class_weight={1: 10})
wclf.fit(X, y)
```
