# Reconstruir y deshacerse del ruido en las imágenes de prueba

Transformamos y reconstruimos el conjunto de prueba con ruido utilizando tanto PCA como Kernel PCA. Luego graficamos las imágenes reconstruidas para comparar los resultados.

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(
    kernel_pca.transform(X_test_noisy)
)
X_reconstructed_pca = pca.inverse_transform(pca.transform(X_test_noisy))

plot_digits(X_test, "Imágenes de prueba sin ruido")
plot_digits(
    X_reconstructed_pca,
    f"Reconstrucción con PCA\nMSE: {np.mean((X_test - X_reconstructed_pca) ** 2):.2f}",
)
plot_digits(
    X_reconstructed_kernel_pca,
    (
        "Reconstrucción con Kernel PCA\n"
        f"MSE: {np.mean((X_test - X_reconstructed_kernel_pca) ** 2):.2f}"
    ),
)
```
