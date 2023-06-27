# Train the Model

We will now train the SGDClassifier model on the iris dataset with the help of the fit() method. This method takes the input data and target values as input and trains the model on the given data.

```python
clf = SGDClassifier(alpha=0.001, max_iter=100).fit(X, y)
```
