# Führe die Faktorenanalyse mit Varimax-Drehung durch

Wir führen jetzt die Faktorenanalyse auf dem Iris-Datensatz mit Varimax-Drehung durch, um die zugrunde liegende Struktur der Daten zu enthüllen. Wir werden die Ergebnisse mit der PCA und der nicht gedrehten Faktorenanalyse vergleichen.

```python
# Führe die Faktorenanalyse mit Varimax-Drehung durch
n_comps = 2

methods = [
    ("PCA", PCA()),
    ("Nicht gedrehte FA", FactorAnalysis()),
    ("Varimax FA", FactorAnalysis(rotation="varimax")),
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
    ax.set_xticklabels(["Komponente 1", "Komponente 2"])
fig.suptitle("Faktoren")
plt.tight_layout()
plt.show()
```
