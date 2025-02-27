# Zeichnen des PCA-Spektrums

Wir zeichnen das PCA-Spektrum, um das erklärte Varianzverhältnis jeder Hauptkomponente zu visualisieren.

```python
pca.fit(X_digits)

fig, (ax0, ax1) = plt.subplots(nrows=2, sharex=True, figsize=(6, 6))
ax0.plot(
    np.arange(1, pca.n_components_ + 1), pca.explained_variance_ratio_, "+", linewidth=2
)
ax0.set_ylabel("PCA erklärtes Varianzverhältnis")

ax0.axvline(
    search.best_estimator_.named_steps["pca"].n_components,
    linestyle=":",
    label="n_components gewählt",
)
ax0.legend(prop=dict(size=12))
```
