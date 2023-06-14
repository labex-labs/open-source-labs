# Train and test the Logistic Regression classifier

We will now train a Logistic Regression classifier using scikit-learn's `LogisticRegression` function and test it on the testing set. We will then print the accuracy score of the classifier.

```python
from sklearn.linear_model import LogisticRegression

logistic = LogisticRegression(max_iter=1000)
logistic.fit(X_train, y_train)
logistic_score = logistic.score(X_test, y_test)

print("Logistic Regression score: %f" % logistic_score)
```


