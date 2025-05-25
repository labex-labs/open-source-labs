# Avaliar o Modelo

Avaliaremos o desempenho do modelo calculando a esparcidade e a pontuação de precisão.

```python
sparsity = np.mean(clf.coef_ == 0) * 100
score = clf.score(X_test, y_test)

print("Esparsidade com penalidade L1: %.2f%%" % sparsity)
print("Pontuação de teste com penalidade L1: %.4f" % score)
```
