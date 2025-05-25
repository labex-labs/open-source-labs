# Visualizar as projeções PCA e PCA Kernel

Vamos plotar as projeções PCA e PCA Kernel para visualizar as diferenças entre elas.

```python
fig, (orig_data_ax, pca_proj_ax, kernel_pca_proj_ax) = plt.subplots(
    ncols=3, figsize=(14, 4)
)

orig_data_ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test)
orig_data_ax.set_ylabel("Característica #1")
orig_data_ax.set_xlabel("Característica #0")
orig_data_ax.set_title("Dados de teste")

pca_proj_ax.scatter(X_test_pca[:, 0], X_test_pca[:, 1], c=y_test)
pca_proj_ax.set_ylabel("Componente principal #1")
pca_proj_ax.set_xlabel("Componente principal #0")
pca_proj_ax.set_title("Projeção dos dados de teste\n usando PCA")

kernel_pca_proj_ax.scatter(X_test_kernel_pca[:, 0], X_test_kernel_pca[:, 1], c=y_test)
kernel_pca_proj_ax.set_ylabel("Componente principal #1")
kernel_pca_proj_ax.set_xlabel("Componente principal #0")
_ = kernel_pca_proj_ax.set_title("Projeção dos dados de teste\n usando KernelPCA")
```
