# Erstellen eines SVM-Modells

Wir werden ein lineares SVM-Modell mit SGD-Training erstellen.

```python
# Erstellen eines SVM-Modells mit SGD-Training
clf = SGDClassifier(loss="hinge", penalty="elasticnet", fit_intercept=True)
```
