# Application de la pénalité Elastic-Net

Nous allons maintenant appliquer la pénalité Elastic-Net sur nos données en utilisant SGDClassifier.

```python
# Créer un classifieur avec la pénalité Elastic-Net
clf = SGDClassifier(loss='hinge', penalty='elasticnet', alpha=0.05, l1_ratio=0.15, max_iter=1000, tol=1e-3)

# Ajuster le modèle
clf.fit(X, y)

# Tracer la frontière de décision
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
plt.title('Pénalité Elastic-Net')
plt.show()
```
