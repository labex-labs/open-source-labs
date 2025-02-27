# Modelle trainieren

Wir werden zwei SVM-Modelle erstellen. Das erste Modell wird die Stichprobengewichte nicht berücksichtigen, und das zweite Modell wird die von uns gerade erstellten Stichprobengewichte berücksichtigen.

```python
clf_no_weights = svm.SVC(gamma=1)
clf_no_weights.fit(X, y)

clf_weights = svm.SVC(gamma=1)
clf_weights.fit(X, y, sample_weight=sample_weight_last_ten)
```
