# Ajuster le modèle

Nous allons ajuster le modèle et obtenir l'hyperplan de séparation à l'aide de la fonction `SVC` de la bibliothèque `svm`. Nous utiliserons un noyau linéaire et définirons `C` sur 1,0.

```python
clf = svm.SVC(kernel="linear", C=1.0)
clf.fit(X, y)
```
