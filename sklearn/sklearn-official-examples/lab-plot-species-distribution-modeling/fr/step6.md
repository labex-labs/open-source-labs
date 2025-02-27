# Prédire la distribution d'espèces

Dans cette étape, nous allons prédire la distribution d'espèces en utilisant le modèle OneClassSVM. Nous allons prédire la distribution d'espèces en utilisant les données d'entraînement et tracer les résultats.

```python
# Prédire la distribution d'espèces en utilisant les données d'entraînement
Z = np.ones((data.Ny, data.Nx), dtype=np.float64)

# Nous ne prédirons que pour les points terrestres.
idx = np.where(data.coverages[6] > -9999)
coverages_land = data.coverages[:, idx[0], idx[1]].T

pred = clf.decision_function((coverages_land - mean) / std)
Z *= pred.min()
Z[idx[0], idx[1]] = pred

levels = np.linspace(Z.min(), Z.max(), 25)
Z[data.coverages[6] == -9999] = -9999

# tracer les contours de la prédiction
plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.Reds)
plt.colorbar(format="%.2f")

# disperser les points d'entraînement/test
plt.scatter(
    BV_bunch.pts_train["dd long"],
    BV_bunch.pts_train["dd lat"],
    s=2**2,
    c="black",
    marqueur="^",
    label="train",
)
plt.scatter(
    BV_bunch.pts_test["dd long"],
    BV_bunch.pts_test["dd lat"],
    s=2**2,
    c="black",
    marqueur="x",
    label="test",
)
plt.legend()
plt.title(BV_bunch.name)
plt.axe("égal")
```
