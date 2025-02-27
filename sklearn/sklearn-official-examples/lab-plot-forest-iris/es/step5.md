# Trazar superficies de decisión

En este paso, trazaremos las superficies de decisión de los modelos definidos en el conjunto de datos iris.

```python
plot_idx = 1

for pair in ([0, 1], [0, 2], [2, 3]):
    for model in models:
        # Solo tomamos las dos características correspondientes
        X = iris.data[:, pair]
        y = iris.target

        # Mezclar
        idx = np.arange(X.shape[0])
        np.random.seed(RANDOM_SEED)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

        # Estandarizar
        mean = X.mean(axis=0)
        std = X.std(axis=0)
        X = (X - mean) / std

        # Entrenar
        model.fit(X, y)

        scores = model.score(X, y)
        # Crear un título para cada columna y la consola usando str() y
        # cortando partes inútiles de la cadena
        model_title = str(type(model)).split(".")[-1][:-2][: -len("Classifier")]

        model_details = model_title
        if hasattr(model, "estimators_"):
            model_details += " con {} estimadores".format(len(model.estimators_))
        print(model_details + " con características", pair, "tiene una puntuación de", scores)

        plt.subplot(3, 4, plot_idx)
        if plot_idx <= len(models):
            # Agregar un título en la parte superior de cada columna
            plt.title(model_title, fontsize=9)

        # Ahora trazar el límite de decisión usando una malla fina como entrada a un
        # trazado de contorno relleno
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(
            np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step)
        )

        # Trazar ya sea un solo DecisionTreeClassifier o mezclar alfa
        # las superficies de decisión del conjunto de clasificadores
        if isinstance(model, DecisionTreeClassifier):
            Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            cs = plt.contourf(xx, yy, Z, cmap=cmap)
        else:
            # Elegir el nivel de mezcla alfa con respecto al número
            # de estimadores
            # que se están usando (teniendo en cuenta que AdaBoost puede usar menos estimadores
            # que su máximo si alcanza una ajuste lo suficientemente bueno al principio)
            estimator_alpha = 1.0 / len(model.estimators_)
            for tree in model.estimators_:
                Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])
                Z = Z.reshape(xx.shape)
                cs = plt.contourf(xx, yy, Z, alpha=estimator_alpha, cmap=cmap)

        # Construir una malla más gruesa para trazar un conjunto de clasificaciones del conjunto
        # para mostrar cómo estas son diferentes a lo que vemos en las decisiones
        # superficies. Estos puntos están regularmente espaciados y no tienen un
        # contorno negro
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

        # Trazar los puntos de entrenamiento, estos están agrupados juntos y tienen un
        # contorno negro
        plt.scatter(
            X[:, 0],
            X[:, 1],
            c=y,
            cmap=ListedColormap(["r", "y", "b"]),
            edgecolor="k",
            s=20,
        )
        plot_idx += 1  # pasar al siguiente trazado en secuencia

plt.suptitle("Clasificadores en subconjuntos de características del conjunto de datos Iris", fontsize=12)
plt.axis("tight")
plt.tight_layout(h_pad=0.2, w_pad=0.2, pad=2.5)
plt.show()
```
