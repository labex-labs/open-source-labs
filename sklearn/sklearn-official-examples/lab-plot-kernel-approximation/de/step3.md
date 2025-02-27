# Entscheidungsflächen von RBF-Kernel-SVM und linearem SVM

```python
# Visualisiere die Entscheidungsfläche, projiziert auf die ersten
# zwei Hauptkomponenten des Datensatzes
pca = PCA(n_components=8).fit(data_train)

X = pca.transform(data_train)

# Generiere Gitter entlang der ersten beiden Hauptkomponenten
multiples = np.arange(-2, 2, 0.1)
# Schritte entlang der ersten Komponente
first = multiples[:, np.newaxis] * pca.components_[0, :]
# Schritte entlang der zweiten Komponente
second = multiples[:, np.newaxis] * pca.components_[1, :]
# Kombiniere
grid = first[np.newaxis, :, :] + second[:, np.newaxis, :]
flat_grid = grid.reshape(-1, data.shape[1])

# Titel für die Plots
titles = [
    "SVC mit rbf-Kernel",
    "SVC (linearer Kernel)\n mit Fourier rbf-Feature-Map\nn_components=100",
    "SVC (linearer Kernel)\n mit Nystroem rbf-Feature-Map\nn_components=100",
]

plt.figure(figsize=(18, 7.5))
plt.rcParams.update({"font.size": 14})
# Vorhersage und Plot
for i, clf in enumerate((kernel_svm, nystroem_approx_svm, fourier_approx_svm)):
    # Zeichne die Entscheidungsgrenze. Dazu werden wir jeder
    # Punkt im Gitter [x_min, x_max]x[y_min, y_max] eine Farbe zuweisen.
    plt.subplot(1, 3, i + 1)
    Z = clf.predict(flat_grid)

    # Bringe das Ergebnis in einen Farbplot
    Z = Z.reshape(grid.shape[:-1])
    levels = np.arange(10)
    lv_eps = 0.01  # Anpassen einer Zuordnung von berechneten Kontur-Ebenen zu Farben.
    plt.contourf(
        multiples,
        multiples,
        Z,
        levels=levels - lv_eps,
        cmap=plt.cm.tab10,
        vmin=0,
        vmax=10,
        alpha=0.7,
    )
    plt.axis("off")

    # Zeichne auch die Trainingspunkte
    plt.scatter(
        X[:, 0],
        X[:, 1],
        c=targets_train,
        cmap=plt.cm.tab10,
        edgecolors=(0, 0, 0),
        vmin=0,
        vmax=10,
    )

    plt.title(titles[i])
plt.tight_layout()
plt.show()
```
