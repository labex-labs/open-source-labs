# Visualizar o conjunto de dados reconstruído

Vamos plotar o conjunto de dados original e o conjunto de dados reconstruído para compará-los.

```python
fig, (orig_data_ax, pca_back_proj_ax, kernel_pca_back_proj_ax) = plt.subplots(
    ncols=3, sharex=True, sharey=True, figsize=(13, 4)
)

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Característica #1")
orig_data_ax.set_xlabel("Característica #0")
orig_data_ax.set_title("Dados de teste originais")

pca_back_proj_ax.scatter(X_reconstructed_pca[:, 0], X_reconstructed_pca[:, 1], c=y_test)
pca_back_proj_ax.set_xlabel("Característica #0")
pca_back_proj_ax.set_title("Reconstrução via PCA")

kernel_pca_back_proj_ax.scatter(
    X_reconstructed_kernel_pca[:, 0], X_reconstructed_kernel_pca[:, 1], c=y_test
)
kernel_pca_back_proj_ax.set_xlabel("Característica #0")
_ = kernel_pca_back_proj_ax.set_title("Reconstrução via KernelPCA")
```
