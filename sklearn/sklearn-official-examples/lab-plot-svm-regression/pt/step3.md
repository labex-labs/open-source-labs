# Visualizar Resultados

Finalmente, visualizamos os resultados dos nossos modelos SVR traçando-os contra o conjunto de dados de amostra. Também representamos os vetores de suporte e outros dados de treino.

```python
import matplotlib.pyplot as plt

# Examinar os resultados
lw = 2

kernel_label = ["RBF", "Linear", "Polinomial"]
model_color = ["m", "c", "g"]

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 10), sharey=True)

for ix, svr in enumerate(svrs):
    axes[ix].plot(
        X,
        svr.predict(X),
        color=model_color[ix],
        lw=lw,
        label="Modelo {}".format(kernel_label[ix]),
    )
    axes[ix].scatter(
        X[svr.support_],
        y[svr.support_],
        facecolor="none",
        edgecolor=model_color[ix],
        s=50,
        label="Vetores de suporte {}".format(kernel_label[ix]),
    )
    axes[ix].scatter(
        X[np.setdiff1d(np.arange(len(X)), svr.support_)],
        y[np.setdiff1d(np.arange(len(X)), svr.support_)],
        facecolor="none",
        edgecolor="k",
        s=50,
        label="Outros dados de treino",
    )
    axes[ix].legend(
        loc="upper center",
        bbox_to_anchor=(0.5, 1.1),
        ncol=1,
        fancybox=True,
        shadow=True,
    )

fig.text(0.5, 0.04, "dados", ha="center", va="center")
fig.text(0.06, 0.5, "alvo", ha="center", va="center", rotation="vertical")
fig.suptitle("Regressão Vetorial de Suporte", fontsize=14)
plt.show()
```
