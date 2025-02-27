# Exécuter l'analyse factorielle avec rotation Varimax

Nous allons maintenant exécuter l'analyse factorielle sur l'ensemble de données Iris avec rotation Varimax pour découvrir la structure sous-jacente des données. Nous comparerons les résultats avec la PCA et l'AF non tournée.

```python
# Exécuter l'analyse factorielle avec rotation Varimax
n_comps = 2

methods = [
    ("PCA", PCA()),
    ("AF non tournée", FactorAnalysis()),
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
fig.suptitle("Facteurs")
plt.tight_layout()
plt.show()
```
