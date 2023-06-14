# Train the SVM model with SGD

Next, we need to train the SVM model using SGD. We will use the `SGDClassifier` class from Scikit-learn to train the model. We will set the `loss` parameter to "hinge" to use the SVM algorithm and the `alpha` parameter to 0.01 to control the regularization strength. We will also set the `max_iter` parameter to 200 to limit the number of iterations.

```python
# fit the model
clf = SGDClassifier(loss="hinge", alpha=0.01, max_iter=200)
clf.fit(X, Y)
```


