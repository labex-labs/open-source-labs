# Visualizar el conjunto de datos reconstruido

Graficaremos el conjunto de datos original y el conjunto de datos reconstruido para compararlos.

```python
fig, (orig_data_ax, pca_back_proj_ax, kernel_pca_back_proj_ax) = plt.subplots(
    ncols=3, sharex=True, sharey=True, figsize=(13, 4)
)

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Característica #1")
orig_data_ax.set_xlabel("Característica #0")
orig_data_ax.set_title("Datos de prueba originales")

pca_back_proj_ax.scatter(X_reconstructed_pca[:, 0], X_reconstructed_pca[:, 1], c=y_test)
pca_back_proj_ax.set_xlabel("Característica #0")
pca_back_proj_ax.set_title("Reconstrucción a través de PCA")

kernel_pca_back_proj_ax.scatter(
    X_reconstructed_kernel_pca[:, 0], X_reconstructed_kernel_pca[:, 1], c=y_test
)
kernel_pca_back_proj_ax.set_xlabel("Característica #0")
_ = kernel_pca_back_proj_ax.set_title("Reconstrucción a través de KernelPCA")
```
