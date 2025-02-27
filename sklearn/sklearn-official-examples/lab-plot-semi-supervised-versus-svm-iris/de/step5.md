# Visualisiere die Entscheidungsgrenzen

Wir werden ein Gitternetz von Punkten erstellen, das den Eingangsmerkmalraum abdeckt, und jede Klassifizierung verwenden, um die Labels für die Punkte im Gitternetz vorherzusagen. Anschließend werden wir die Entscheidungsgrenzen und die markierten Datenpunkte plotten.

```python
# Erstelle ein Gitternetz zum Plotten
h = 0.02
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

# Definiere eine Farbkarte für die Labels
color_map = {-1: (1, 1, 1), 0: (0, 0, 0.9), 1: (1, 0, 0), 2: (0.8, 0.6, 0)}

# Setze die Klassifizierer ein
classifiers = (ls30, st30, ls50, st50, ls100, rbf_svc)

# Plot die Entscheidungsgrenzen und die markierten Datenpunkte für jede Klassifizierung
for i, (clf, y_train, title) in enumerate(classifiers):
    # Plot die Entscheidungsgrenze
    plt.subplot(3, 2, i + 1)
    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Bringe das Ergebnis in einen Farbplot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)
    plt.axis("off")

    # Plot die markierten Datenpunkte
    colors = [color_map[y] for y in y_train]
    plt.scatter(X[:, 0], X[:, 1], c=colors, edgecolors="black")

    plt.title(title)

plt.suptitle("Unmarkierte Punkte sind weiß gefärbt", y=0.1)
plt.show()
```
