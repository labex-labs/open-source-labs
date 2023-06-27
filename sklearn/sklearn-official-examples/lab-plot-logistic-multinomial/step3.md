# Train Multinomial Logistic Regression Model

We will now train a multinomial logistic regression model using the `LogisticRegression` function from scikit-learn. We will set the solver to `"sag"`, the maximum number of iterations to 100, the random state to 42, and the multi-class option to `"multinomial"`. We will then print the training score of the model.

```python
clf = LogisticRegression(
        solver="sag", max_iter=100, random_state=42, multi_class="multinomial"
    ).fit(X, y)

print("training score : %.3f (%s)" % (clf.score(X, y), "multinomial"))
```
