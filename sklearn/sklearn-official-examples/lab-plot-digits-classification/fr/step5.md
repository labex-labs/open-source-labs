# Entraîner la machine à vecteurs de support

Nous allons entraîner un classifieur à vecteurs de support sur les échantillons d'entraînement en utilisant la méthode `svm.SVC()` de `sklearn`.

```python
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
```
