# Superfícies de Decisão do Kernel RBF SVM e SVM Linear

```python
# visualizar a superfície de decisão, projetada para os dois primeiros
# componentes principais do conjunto de dados
pca = PCA(n_components=8).fit(data_train)

X = pca.transform(data_train)

# Gerar grade ao longo dos dois primeiros componentes principais
multiples = np.arange(-2, 2, 0.1)
# passos ao longo do primeiro componente
first = multiples[:, np.newaxis] * pca.components_[0, :]
# passos ao longo do segundo componente
second = multiples[:, np.newaxis] * pca.components_[1, :]
# combinar
grid = first[np.newaxis, :, :] + second[:, np.newaxis, :]
flat_grid = grid.reshape(-1, data.shape[1])

# título para os gráficos
titles = [
    "SVC com kernel rbf",
    "SVC (kernel linear)\n com mapa de características rbf Fourier\nn_components=100",
    "SVC (kernel linear)\n com mapa de características rbf Nystroem\nn_components=100",
]

plt.figure(figsize=(18, 7.5))
plt.rcParams.update({"font.size": 14})
# prever e plotar
for i, clf in enumerate((kernel_svm, nystroem_approx_svm, fourier_approx_svm)):
    # Plotar a fronteira de decisão. Para isso, atribuiremos uma cor a cada
    # ponto na malha [x_min, x_max]x[y_min, y_max].
    plt.subplot(1, 3, i + 1)
    Z = clf.predict(flat_grid)

    # Colocar o resultado num gráfico de cores
    Z = Z.reshape(grid.shape[:-1])
    levels = np.arange(10)
    lv_eps = 0.01  # Ajustar um mapeamento dos níveis de contorno calculados para a cor.
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

    # Plotar também os pontos de treino
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
