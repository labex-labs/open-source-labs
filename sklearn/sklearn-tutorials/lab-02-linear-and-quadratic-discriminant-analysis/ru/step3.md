# Обучение и визуализация классификаторов

Теперь мы обучим классификаторы LDA и QDA на синтетических данных и визуализируем границы принятия решений.

```python
# Train the LDA classifier
lda = LinearDiscriminantAnalysis()
lda.fit(X, y)

# Train the QDA classifier
qda = QuadraticDiscriminantAnalysis()
qda.fit(X, y)

# Plot the decision boundaries
def plot_decision_boundary(classifier, title):
    h = 0.02  # step size in the mesh
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Paired)
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title(title)

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plot_decision_boundary(lda, 'Linear Discriminant Analysis')

plt.subplot(1, 2, 2)
plot_decision_boundary(qda, 'Quadratic Discriminant Analysis')

plt.tight_layout()
plt.show()
```
