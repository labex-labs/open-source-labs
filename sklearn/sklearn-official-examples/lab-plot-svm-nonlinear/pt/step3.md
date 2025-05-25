# Treinar o Modelo

Neste passo, treinaremos o classificador SVM com o kernel RBF utilizando os dados gerados.

```python
clf = svm.NuSVC(gamma="auto")
clf.fit(X, Y)
```
