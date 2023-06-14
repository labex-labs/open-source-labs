# Predict Species Distribution

In this step, we will predict the species distribution using the OneClassSVM model. We will predict the species distribution using the training data and plot the results.

```python
# Predict species distribution using the training data
Z = np.ones((data.Ny, data.Nx), dtype=np.float64)

# We'll predict only for the land points.
idx = np.where(data.coverages[6] > -9999)
coverages_land = data.coverages[:, idx[0], idx[1]].T

pred = clf.decision_function((coverages_land - mean) / std)
Z *= pred.min()
Z[idx[0], idx[1]] = pred

levels = np.linspace(Z.min(), Z.max(), 25)
Z[data.coverages[6] == -9999] = -9999

# plot contours of the prediction
plt.contourf(X, Y, Z, levels=levels, cmap=plt.cm.Reds)
plt.colorbar(format="%.2f")

# scatter training/testing points
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


