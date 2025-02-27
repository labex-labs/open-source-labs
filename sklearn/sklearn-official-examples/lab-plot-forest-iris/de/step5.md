# Entscheidungsflächen darstellen

In diesem Schritt werden wir die Entscheidungsflächen der definierten Modelle auf dem Iris-Datensatz darstellen.

```python
plot_idx = 1

for pair in ([0, 1], [0, 2], [2, 3]):
    for model in models:
        # Wir nehmen nur die zwei entsprechenden Merkmale
        X = iris.data[:, pair]
        y = iris.target

        # Mischen
        idx = np.arange(X.shape[0])
        np.random.seed(RANDOM_SEED)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

        # Standardisieren
        mean = X.mean(axis=0)
        std = X.std(axis=0)
        X = (X - mean) / std

        # Trainieren
        model.fit(X, y)

        scores = model.score(X, y)
        # Erstellen Sie einen Titel für jede Spalte und die Konsole, indem Sie str() verwenden und
        # abschneiden Sie nutzlose Teile der Zeichenfolge
        model_title = str(type(model)).split(".")[-1][:-2][: -len("Classifier")]

        model_details = model_title
        if hasattr(model, "estimators_"):
            model_details += " mit {} Schätzern".format(len(model.estimators_))
        print(model_details + " mit Merkmalen", pair, "hat einen Score von", scores)

        plt.subplot(3, 4, plot_idx)
        if plot_idx <= len(models):
            # Fügen Sie einen Titel oben jeder Spalte hinzu
            plt.title(model_title, fontsize=9)

        # Nun zeichnen Sie die Entscheidungsgrenze mit einem feinen Gitter als Eingabe für eine
        # gefüllte Konturlinie
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(
            np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step)
        )

        # Zeichnen Sie entweder einen einzelnen DecisionTreeClassifier oder mischen Sie alpha
        # die Entscheidungsflächen des Ensembles von Klassifizierern
        if isinstance(model, DecisionTreeClassifier):
            Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            cs = plt.contourf(xx, yy, Z, cmap=cmap)
        else:
            # Wählen Sie das Alpha-Mischlevel im Bezug auf die Anzahl
            # der Schätzer
            # die in Verwendung sind (beachten Sie, dass AdaBoost möglicherweise weniger Schätzer verwenden kann
            # als sein Maximum, wenn es frühzeitig eine ausreichend gute Anpassung erreicht)
            estimator_alpha = 1.0 / len(model.estimators_)
            for tree in model.estimators_:
                Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])
                Z = Z.reshape(xx.shape)
                cs = plt.contourf(xx, yy, Z, alpha=estimator_alpha, cmap=cmap)

        # Erstellen Sie ein groberes Gitter, um eine Reihe von Ensemble-Klassifikationen zu zeichnen
        # um zu zeigen, wie diese sich von dem unterscheiden, was wir in den Entscheidungsflächen sehen
        # Flächen. Diese Punkte sind regelmäßig verteilt und haben keinen schwarzen Umriss
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

        # Zeichnen Sie die Trainingspunkte, diese sind zusammengefasst und haben einen
        # schwarzen Umriss
        plt.scatter(
            X[:, 0],
            X[:, 1],
            c=y,
            cmap=ListedColormap(["r", "y", "b"]),
            edgecolor="k",
            s=20,
        )
        plot_idx += 1  # Gehen Sie zum nächsten Plot in der Sequenz über

plt.suptitle("Klassifizierer auf Merkmalsuntermengen des Iris-Datensatzes", fontsize=12)
plt.axis("tight")
plt.tight_layout(h_pad=0.2, w_pad=0.2, pad=2.5)
plt.show()
```
