# Visualizar Resultados

Vamos visualizar os resultados de IPCA e PCA, plotando os dados transformados num gráfico de dispersão.

```python
colors = ["navy", "turquoise", "darkorange"]

for X_transformed, title in [(X_ipca, "IPCA Incremental"), (X_pca, "PCA")]:
    plt.figure(figsize=(8, 8))
    for color, i, target_name in zip(colors, [0, 1, 2], iris.target_names):
        plt.scatter(
            X_transformed[y == i, 0],
            X_transformed[y == i, 1],
            color=color,
            lw=2,
            label=target_name,
        )

    if "Incremental" in title:
        err = np.abs(np.abs(X_pca) - np.abs(X_ipca)).mean()
        plt.title(title + " do conjunto de dados iris\nErro médio absoluto não assinado %.6f" % err)
    else:
        plt.title(title + " do conjunto de dados iris")
    plt.legend(loc="best", shadow=False, scatterpoints=1)
    plt.axis([-4, 4, -1.5, 1.5])

plt.show()
```
