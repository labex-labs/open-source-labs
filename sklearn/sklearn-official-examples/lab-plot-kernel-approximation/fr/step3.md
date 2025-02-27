# Surfaces de décision du SVM à noyau RBF et du SVM linéaire

```python
# visualisez la surface de décision, projetée sur les deux premières
# composantes principales du jeu de données
pca = PCA(n_components=8).fit(data_train)

X = pca.transform(data_train)

# Générez une grille le long des deux premières composantes principales
multiples = np.arange(-2, 2, 0.1)
# pas le long de la première composante
first = multiples[:, np.newaxis] * pca.components_[0, :]
# pas le long de la deuxième composante
second = multiples[:, np.newaxis] * pca.components_[1, :]
# combinez
grid = first[np.newaxis, :, :] + second[:, np.newaxis, :]
flat_grid = grid.reshape(-1, data.shape[1])

# titre pour les graphiques
titles = [
    "SVC avec noyau rbf",
    "SVC (noyau linéaire)\n avec carte de caractéristiques rbf de Fourier\nn_components=100",
    "SVC (noyau linéaire)\n avec carte de caractéristiques rbf de Nystroem\nn_components=100",
]

plt.figure(figsize=(18, 7.5))
plt.rcParams.update({"font.size": 14})
# prédisez et tracez
for i, clf in enumerate((kernel_svm, nystroem_approx_svm, fourier_approx_svm)):
    # Tracez la frontière de décision. Pour cela, nous allons attribuer une couleur à chaque
    # point dans la grille [x_min, x_max]x[y_min, y_max].
    plt.subplot(1, 3, i + 1)
    Z = clf.predict(flat_grid)

    # Placez le résultat dans un graphique en couleur
    Z = Z.reshape(grid.shape[:-1])
    levels = np.arange(10)
    lv_eps = 0.01  # Ajustez une correspondance entre les niveaux de contour calculés et la couleur.
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

    # Tracez également les points d'entraînement
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
