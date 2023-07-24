# Plot the Maximum Margin Separating Hyperplane

To plot the maximum margin separating hyperplane, we will use the `DecisionBoundaryDisplay.from_estimator()` function from scikit-learn. This function plots the decision function and the support vectors of the SVM classifier. We will also plot the support vectors as circles with no fill and a black edge.

```python
from sklearn.inspection import DecisionBoundaryDisplay

# plot the decision function and support vectors
ax = plt.gca()
DecisionBoundaryDisplay.from_estimator(
    clf,
    X,
    plot_method="contour",
    colors="k",
    levels=[-1, 0, 1],
    alpha=0.5,
    linestyles=["--", "-", "--"],
    ax=ax,
)
ax.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=100,
    linewidth=1,
    facecolors="none",
    edgecolors="k",
)
plt.show()
```
