# Visualisierung der Entscheidungsfunktion

In diesem Schritt werden wir die Entscheidungsfunktion visualisieren, die von der Support Vector Machine (SVM) gelernt wurde. Wir erstellen ein Raster von Punkten und verwenden den SVM-Klassifikator, um die Klasse jedes Punktes vorherzusagen. Anschließend zeichnen wir die Punkte mit ihren jeweiligen Klassen sowie die Entscheidungsgrenze, die von der SVM gelernt wurde.

```python
xx, yy = np.meshgrid(np.linspace(-3, 3, 500), np.linspace(-3, 3, 500))
Z = clf.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

plt.imshow(
    Z,
    interpolation="nearest",
    extent=(xx.min(), xx.max(), yy.min(), yy.max()),
    aspect="auto",
    origin="lower",
    cmap=plt.cm.PuOr_r,
)
contours = plt.contour(xx, yy, Z, levels=[0], linewidths=2, linestyles="dashed")
plt.scatter(X[:, 0], X[:, 1], s=30, c=Y, cmap=plt.cm.Paired, edgecolors="k")
plt.xticks(())
plt.yticks(())
plt.axis([-3, 3, -3, 3])
plt.show()
```
