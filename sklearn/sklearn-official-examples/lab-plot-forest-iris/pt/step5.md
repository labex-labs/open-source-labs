# Traçar Superfícies de Decisão

Neste passo, traçaremos as superfícies de decisão dos modelos definidos no conjunto de dados iris.

```python
plot_idx = 1

for pair in ([0, 1], [0, 2], [2, 3]):
    for model in models:
        # Apenas as duas características correspondentes são utilizadas
        X = iris.data[:, pair]
        y = iris.target

        # Embaralhamento
        idx = np.arange(X.shape[0])
        np.random.seed(RANDOM_SEED)
        np.random.shuffle(idx)
        X = X[idx]
        y = y[idx]

        # Padronização
        mean = X.mean(axis=0)
        std = X.std(axis=0)
        X = (X - mean) / std

        # Treinamento
        model.fit(X, y)

        scores = model.score(X, y)
        # Cria um título para cada coluna e o console usando str() e
        # removendo partes desnecessárias da string
        model_title = str(type(model)).split(".")[-1][:-2][: -len("Classifier")]

        model_details = model_title
        if hasattr(model, "estimators_"):
            model_details += " com {} estimadores".format(len(model.estimators_))
        print(model_details + " com características", pair, "tem uma pontuação de", scores)

        plt.subplot(3, 4, plot_idx)
        if plot_idx <= len(models):
            # Adiciona um título no topo de cada coluna
            plt.title(model_title, fontsize=9)

        # Agora plota o limite de decisão usando uma malha fina como entrada para um gráfico de contorno preenchido
        x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
        y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
        xx, yy = np.meshgrid(
            np.arange(x_min, x_max, plot_step), np.arange(y_min, y_max, plot_step)
        )

        # Plota um único DecisionTreeClassifier ou mescla alfa as superfícies de decisão do conjunto de classificadores
        if isinstance(model, DecisionTreeClassifier):
            Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)
            cs = plt.contourf(xx, yy, Z, cmap=cmap)
        else:
            # Escolhe o nível de mescla alfa em relação ao número
            # de estimadores
            # que estão em uso (observando que o AdaBoost pode usar menos estimadores
            # do que o máximo se atingir um ajuste suficientemente bom no início)
            estimator_alpha = 1.0 / len(model.estimators_)
            for tree in model.estimators_:
                Z = tree.predict(np.c_[xx.ravel(), yy.ravel()])
                Z = Z.reshape(xx.shape)
                cs = plt.contourf(xx, yy, Z, alpha=estimator_alpha, cmap=cmap)

        # Cria uma malha mais grosseira para plotar um conjunto de classificações de conjunto para mostrar como elas são diferentes do que vemos nas superfícies de decisão. Esses pontos são regularmente espaçados e não têm um contorno preto
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

        # Plota os pontos de treinamento, estes estão agrupados e têm um contorno preto
        plt.scatter(
            X[:, 0],
            X[:, 1],
            c=y,
            cmap=ListedColormap(["r", "y", "b"]),
            edgecolor="k",
            s=20,
        )
        plot_idx += 1  # Avança para o próximo gráfico na sequência

plt.suptitle("Classificadores em subconjuntos de características do conjunto de dados Iris", fontsize=12)
plt.axis("tight")
plt.tight_layout(h_pad=0.2, w_pad=0.2, pad=2.5)
plt.show()
```
