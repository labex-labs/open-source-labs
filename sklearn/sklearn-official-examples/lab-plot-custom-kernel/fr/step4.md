# Créer un classifieur SVM

Dans cette étape, nous allons créer une instance du classifieur SVM et ajuster nos données. Nous utiliserons le noyau personnalisé créé dans l'étape précédente.

```python
clf = svm.SVC(kernel=my_kernel)
clf.fit(X, Y)
```
