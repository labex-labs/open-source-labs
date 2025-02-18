# Entraînement du modèle

Dans cette étape, nous allons entraîner le classifieur SVM avec un noyau RBF en utilisant les données générées.

```python
clf = svm.NuSVC(gamma="auto")
clf.fit(X, Y)
```
