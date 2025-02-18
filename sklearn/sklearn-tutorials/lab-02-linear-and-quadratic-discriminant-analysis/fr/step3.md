# Entraînement et visualisation des classifieurs

Maintenant, nous allons entraîner les classifieurs LDA et QDA sur les données synthétiques et visualiser les frontières de décision.

```python
# Entraînement du classifieur LDA
lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

# Entraînement du classifieur QDA
qda = QuadraticDiscriminantAnalysis()
qda.fit(X, y)

# Traçage des frontières de décision
def plot_decision_boundary(classifier, title):
    h = 0.02  # Pas dans le maillage
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Paired)
    plt.xlabel('Caractéristique 1')
    plt.ylabel('Caractéristique 2')
    plt.title(title)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plot_decision_boundary(lda, 'Analyse Discriminante Linéaire')

plt.subplot(1, 2, 2)
plot_decision_boundary(qda, 'Analyse Discriminante Quadratique')

plt.tight_layout()
plt.show()
```
