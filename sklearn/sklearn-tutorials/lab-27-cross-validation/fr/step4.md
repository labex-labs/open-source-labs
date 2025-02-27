# Entraînez et évaluez le modèle

Maintenant, entraînons un classifieur à vecteurs de support (SVM) sur l'ensemble d'entraînement et évaluons ses performances sur l'ensemble de test.

```python
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Accuracy: ", score)
```
