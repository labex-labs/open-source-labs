# Visualiser les projections de la PCA et de la PCA Kernel

Nous allons tracer les projections de la PCA et de la PCA Kernel pour visualiser les différences entre elles.

```python
fig, (orig_data_ax, pca_proj_ax, kernel_pca_proj_ax) = plt.subplots(
    ncols=3, figsize=(14, 4)
)

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Feature #1")
orig_data_ax.set_xlabel("Feature #0")
orig_data_ax.set_title("Données de test")

pca_proj_ax.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
pca_proj_ax.set_ylabel("Composante principale #1")
pca_proj_ax.set_xlabel("Composante principale #0")
pca_proj_ax.set_title("Projection des données de test\n en utilisant la PCA")

kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Composante principale #1")
kernel_pca_proj_ax.set_xlabel("Composante principale #0")
_ = kernel_pca_proj_ax.set_title("Projection des données de test\n en utilisant la PCA Kernel")
```
