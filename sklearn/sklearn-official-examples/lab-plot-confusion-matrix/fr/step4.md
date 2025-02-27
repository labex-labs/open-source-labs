# Entraîner le modèle

Nous allons entraîner un classifieur à vecteurs de support (SVM) utilisant un noyau linéaire. Nous utiliserons un paramètre de régularisation C trop bas pour voir l'impact sur les résultats.

```python
classifier = svm.SVC(kernel="linear", C=0.01).fit(X_train, y_train)
```
