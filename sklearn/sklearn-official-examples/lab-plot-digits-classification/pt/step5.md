# Treinar a Máquina de Vetores de Suporte

Vamos treinar um classificador de vetores de suporte nos exemplos de treino utilizando o método `svm.SVC()` da biblioteca `sklearn`.

```python
clf = svm.SVC(gamma=0.001)
clf.fit(X_train, y_train)
```
