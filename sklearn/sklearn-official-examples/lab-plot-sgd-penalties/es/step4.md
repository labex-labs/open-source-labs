# Aplicando la penalización L2

Ahora aplicaremos la penalización L2 a nuestros datos utilizando el SGDClassifier.

```python
# Create a classifier with L2 penalty
clf = SGDClassifier(loss='hinge', penalty='l2', alpha=0.05, max_iter=1000, tol=1e-3)

# Fit the model
clf.fit(X, y)

# Plot the decision boundary
plt.scatter(X[:, 0], X[:, 1], c=y)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx, yy = np.meshgrid(np.linspace(xlim[0], xlim[1], 201), np.linspace(ylim[0], ylim[1], 201))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)
ax.contour(xx, yy, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
ax.set_xlim(xlim)
ax.set_ylim(ylim)
plt.title('Penalización L2')
plt.show()
```
