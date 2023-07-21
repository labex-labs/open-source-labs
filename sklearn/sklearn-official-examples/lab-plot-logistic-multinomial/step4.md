# Plot Decision Boundary of Multinomial Logistic Regression Model

We will now plot the decision surface of the multinomial logistic regression model using the `DecisionBoundaryDisplay` function from scikit-learn. We will set the response method to `"predict"`, the colormap to `"plt.cm.Paired"`, and plot the training points as well.

```python
_, ax = plt.subplots()
DecisionBoundaryDisplay.from_estimator(
        clf, X, response_method="predict", cmap=plt.cm.Paired, ax=ax
    )
plt.title("Decision surface of LogisticRegression (multinomial)")
plt.axis("tight")

colors = "bry"
for i, color in zip(clf.classes_, colors):
        idx = np.where(y == i)
        plt.scatter(
            X[idx, 0], X[idx, 1], c=color, cmap=plt.cm.Paired, edgecolor="black", s=20
        )
```
