# Executar Análise Fatorial com Rotação Varimax

Agora, executaremos a Análise Fatorial no conjunto de dados Iris com rotação Varimax para descobrir a estrutura subjacente dos dados. Compararemos os resultados com PCA e AF não rotacionada.

```python
# Executar análise fatorial com rotação Varimax
n_comps = 2

methods = [
    ("PCA", PCA()),
    ("AF não rotacionada", FactorAnalysis()),
    ("AF Varimax", FactorAnalysis(rotation="varimax")),
]
fig, axes = plt.subplots(ncols=len(methods), figsize=(10, 8), sharey=True)

for ax, (method, fa) in zip(axes, methods):
    fa.set_params(n_components=n_comps)
    fa.fit(X)

    components = fa.components_.T
    print("\n\n %s :\n" % method)
    print(components)

    vmax = np.abs(components).max()
    ax.imshow(components, cmap="RdBu_r", vmax=vmax, vmin=-vmax)
    ax.set_yticks(np.arange(len(feature_names)))
    ax.set_yticklabels(feature_names)
    ax.set_title(str(method))
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Comp. 1", "Comp. 2"])
fig.suptitle("Fatores")
plt.tight_layout()
plt.show()
```
