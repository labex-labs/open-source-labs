# Визуализация границ решения

Мы создадим сетку точек, которая охватывает пространство входных признаков, и будем использовать каждый классификатор для предсказания меток для точек в сетке. Затем мы построим границы решения и помеченные точки данных.

```python
# Create a mesh grid to plot in
h = 0.02
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Define a color map for the labels
color_map = {-1: (1, 1, 1), 0: (0, 0, 0.9), 1: (1, 0, 0), 2: (0.8, 0.6, 0)}

# Set up the classifiers
classifiers = (ls30, st30, ls50, st50, ls100, rbf_svc)

# Plot the decision boundaries and labeled data points for each classifier
for i, (clf, y_train, title) in enumerate(classifiers):
    # Plot the decision boundary
    plt.subplot(3, 2, i + 1)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    plt.axis("off")

    # Plot the labeled data points
    colors = [color_map[y] for y in y_train]
    plt.scatter(X[:, 0], X[:, 1], c=colors, edgecolors="black")

    plt.title(title)

plt.suptitle("Unlabeled points are colored white", y=0.1)
plt.show()
```
