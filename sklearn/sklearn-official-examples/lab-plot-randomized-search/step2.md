# Create an SVM model

We will create a linear SVM model with SGD training.

```python
# create SVM model with SGD training
clf = SGDClassifier(loss="hinge", penalty="elasticnet", fit_intercept=True)
```
