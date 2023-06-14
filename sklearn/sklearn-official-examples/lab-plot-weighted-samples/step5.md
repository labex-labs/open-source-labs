# Plot Decision Functions

We will plot the decision functions of the two models we just created. We will plot the decision function of the first model on the left, and the decision function of the second model on the right. The size of the points will be proportional to their weight.

```python
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))
Z = clf_no_weights.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

axes[0].contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.bone)
axes[0].scatter(X[:, 0], X[:, 1], c=y, s=100 * sample_weight_constant, alpha=0.9, cmap=plt.cm.bone, edgecolors="black")
axes[0].axis("off")
axes[0].set_title("Constant Weights")

Z = clf_weights.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

axes[1].contourf(xx, yy, Z, alpha=0.75, cmap=plt.cm.bone)
axes[1].scatter(X[:, 0], X[:, 1], c=y, s=100 * sample_weight_last_ten, alpha=0.9, cmap=plt.cm.bone, edgecolors="black")
axes[1].axis("off")
axes[1].set_title("Modified Weights")

plt.show()
```
