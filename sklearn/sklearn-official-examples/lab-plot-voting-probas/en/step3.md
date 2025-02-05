# Predict Class Probabilities for all Classifiers

We will predict the class probabilities for all classifiers using the predict_proba() function.

```python
probas = [c.fit(X, y).predict_proba(X) for c in (clf1, clf2, clf3, eclf)]
```
