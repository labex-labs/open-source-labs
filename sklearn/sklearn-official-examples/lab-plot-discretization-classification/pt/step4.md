# Visualizar os Dados

Neste passo, visualizaremos os conjuntos de dados sintéticos de classificação antes da discretização de características. Plotaremos os pontos de treino e teste para cada conjunto de dados.

```python
fig, axes = plt.subplots(
    nrows=len(datasets), ncols=len(classifiers) + 1, figsize=(21, 9)
)

cm_piyg = plt.cm.PiYG
cm_bright = ListedColormap(["#b30065", "#178000"])

# iterar sobre os conjuntos de dados
for ds_cnt, (X, y) in enumerate(datasets):
    print(f"\nconjunto de dados {ds_cnt}\n---------")

    # dividir em partes de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.5, random_state=42
    )

    # criar a malha para as cores de fundo
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    # plotar primeiro o conjunto de dados
    ax = axes[ds_cnt, 0]
    if ds_cnt == 0:
        ax.set_title("Dados de entrada")
    # plotar os pontos de treino
    ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors="k")
    # e os pontos de teste
    ax.scatter(
        X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, alpha=0.6, edgecolors="k"
    )
    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xticks(())
    ax.set_yticks(())
```
