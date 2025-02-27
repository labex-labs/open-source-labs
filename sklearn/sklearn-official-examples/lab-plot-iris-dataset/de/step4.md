# Hauptkomponentenanalyse (PCA) durchführen

Wir werden die Hauptkomponentenanalyse (PCA) durchführen, um die Dimension der Datensammlung zu reduzieren. Wir werden die Daten auf die ersten drei Hauptkomponenten projizieren und die Ergebnisse in 3D darstellen.

```python
fig = plt.figure(1, figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

X_reduced = PCA(n_components=3).fit_transform(iris.data)
ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=y,
    cmap=plt.cm.Set1,
    edgecolor="k",
    s=40,
)

ax.set_title("Erste drei PCA-Richtungen")
ax.set_xlabel("1. Eigenvektor")
ax.xaxis.set_ticklabels([])
ax.set_ylabel("2. Eigenvektor")
ax.yaxis.set_ticklabels([])
ax.set_zlabel("3. Eigenvektor")
ax.zaxis.set_ticklabels([])
```
