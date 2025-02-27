# Modell bewerten

Wir werden die Leistung des Modells bewerten, indem wir die Sparsität und die Genauigkeit berechnen.

```python
sparsity = np.mean(clf.coef_ == 0) * 100
score = clf.score(X_test, y_test)

print("Sparsity with L1 penalty: %.2f%%" % sparsity)
print("Test score with L1 penalty: %.4f" % score)
```
