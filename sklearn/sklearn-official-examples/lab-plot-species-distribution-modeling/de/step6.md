# Artenverteilung vorhersagen

In diesem Schritt werden wir die Artenverteilung mit dem OneClassSVM-Modell vorhersagen. Wir werden die Artenverteilung mit den Trainingsdaten vorhersagen und die Ergebnisse darstellen.

```python
# Predict species distribution using the training data
Z = np.ones((data.Ny, data.Nx), dtype=np.float64)

# Wir werden nur für die Landpunkte vorhersagen.
idx = np.where(data.coverages[6] > -9999)
coverages_land = data.coverages[:, idx[0], idx[1]].T

pred = clf.decision_function((coverages_land - mean) / std)
Z *= pred.min()
Z[idx[0], idx[1]] = pred

levels = np.linspace(Z.min(), Z.max(), 25)
Z[data.coverages[6] == -9999] = -9999

# Zeichne die Konturlinien der Vorhersage
plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.Reds)
plt.colorbar(format="%.2f")

# Streue die Trainings-/Testpunkte
plt.scatter(
    BV_bunch.pts_train["dd long"],
    BV_bunch.pts_train["dd lat"],
    s=2**2,
    c="black",
    marker="^",
    label="train",
)
plt.scatter(
    BV_bunch.pts_test["dd long"],
    BV_bunch.pts_test["dd lat"],
    s=2**2,
    c="black",
    marker="x",
    label="test",
)
plt.legend()
plt.title(BV_bunch.name)
plt.axis("equal")
```
