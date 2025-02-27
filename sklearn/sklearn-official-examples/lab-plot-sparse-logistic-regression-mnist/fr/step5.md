# Évaluer le modèle

Nous allons évaluer les performances du modèle en calculant la rareté et le score de précision.

```python
sparsity = np.mean(clf.coef_ == 0) * 100
score = clf.score(X_test, y_test)

print("Sparsity with L1 penalty: %.2f%%" % sparsity)
print("Test score with L1 penalty: %.4f" % score)
```
