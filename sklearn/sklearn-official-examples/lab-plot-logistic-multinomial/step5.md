# Train One-vs-Rest Logistic Regression Model

We will now train a one-vs-rest logistic regression model using the same parameters as in Step 3, but with the multi-class option set to `"ovr"`. We will then print the training score of the model.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="ovr"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "ovr"))
```
