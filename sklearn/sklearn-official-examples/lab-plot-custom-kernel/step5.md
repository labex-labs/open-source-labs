# Plot Decision Boundary

In this step, we will plot the decision surface and the support vectors. We will use the DecisionBoundaryDisplay module from scikit-learn's inspection module to plot the decision boundary. We will also scatter plot the training points.

```python
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    cmap=plt.cm.Paired,
    ax=ax,
    response_method="predict",
    plot_method="pcolormesh",
    shading="auto",
)

plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolors="k")
plt.title("3-Class classification using Support Vector Machine with custom kernel")
plt.axis("tight")
plt.show()
```
