# Tracer les surfaces de décision

Dans cette étape, nous allons tracer les surfaces de décision des modèles définis sur l'ensemble de données iris.

```python
plot_idx = 1

for pair in ([0, 1], [0, 2], [2, 3]):
    for model in models:
        # Nous ne prenons que les deux caractéristiques correspondantes
        X = iris.data[:, pair]
        y = iris.target

        # Mélange
        idx = np.arange(X.shape[0])
        np.random.seed(RANDOM_SEED)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

        # Standardisation
        mean = X.mean(axis=0)
        std = X.std(axis=0)
        X = (X - mean) / std

        # Entraînement
        model.fit(X, y)

        scores = model.score(X, y)
        # Crée un titre pour chaque colonne et la console en utilisant str() et
        # en coupant les parties inutiles de la chaîne de caractères
        model_title = str(type(model)).split(".")[-1][:-2][: -len("Classifier")]

        model_details = model_title
        if hasattr(model, "estimators_"):
            model_details += " avec {} estimateurs".format(len(model.estimators_))
        print(model_details + " avec les caractéristiques", pair, "a un score de", scores)

        plt.subplot(3, 4, plot_idx)
        if plot_idx <= len(models):
            # Ajoute un titre au sommet de chaque colonne
            plt.title(model_title, fontsize=9)

        # Maintenant, trace la limite de décision en utilisant un maillage fin comme entrée pour un
        # tracé de contour rempli
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(
            np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step)
        )

        # Trace soit un seul DecisionTreeClassifier ou mélange alpha les
        # surfaces de décision de l'ensemble des classifieurs
        if isinstance(model, DecisionTreeClassifier):
            Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            cs = plt.contourf(xx, yy, Z, cmap=cmap)
        else:
            # Choisis le niveau de mélange alpha par rapport au nombre
            # d'estimateurs
            # qui sont utilisés (notant que AdaBoost peut utiliser moins d'estimateurs
            # que son maximum s'il atteint une bonne approximation assez tôt)
            estimator_alpha = 1.0 / len(model.estimators_)
            for tree in model.estimators_:
                Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])
                Z = Z.reshape(xx.shape)
                cs = plt.contourf(xx, yy, Z, alpha=estimator_alpha, cmap=cmap)

        # Construit un maillage plus grossier pour tracer un ensemble de classifications d'ensemble
        # pour montrer comment celles-ci sont différentes de ce que nous voyons dans les
        # surfaces de décision. Ces points sont régulièrement espacés et n'ont pas
        # d'effet de contour noir
        xx_coarser, yy_coarser = np.meshgrid(
            np.arange(x_min, x_max, plot_step_coarser),
            np.arange(y_min, y_max, plot_step_coarser),
        )
        Z_points_coarser = model.predict(
            np.c_[xx_coarser.ravel(), yy_coarser.ravel()]
        ).reshape(xx_coarser.shape)
        cs_points = plt.scatter(
            xx_coarser,
            yy_coarser,
            s=15,
            c=Z_points_coarser,
            cmap=cmap,
            edgecolors="none",
        )

        # Trace les points d'entraînement, ceux-ci sont regroupés et ont un
        # contour noir
        plt.scatter(
            X[:, 0],
            X[:, 1],
            c=y,
            cmap=ListedColormap(["r", "y", "b"]),
            edgecolor="k",
            s=20,
        )
        plot_idx += 1  # passe au prochain tracé dans la séquence

plt.suptitle("Classifieurs sur des sous-ensembles de caractéristiques de l'ensemble de données Iris", fontsize=12)
plt.axis("tight")
plt.tight_layout(h_pad=0.2, w_pad=0.2, pad=2.5)
plt.show()
```
