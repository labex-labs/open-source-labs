# Treinar e avaliar o modelo

Agora, vamos treinar um classificador de máquina de vetores de suporte (SVM) no conjunto de treino e avaliar seu desempenho no conjunto de teste.

```python
clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
score = clf.score(X_test, y_test)
print("Precisão: ", score)
```
