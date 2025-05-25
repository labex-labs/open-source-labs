# Reconstruir e Desruir Ruído em Imagens de Teste

Transformamos e reconstruímos o conjunto de teste ruidoso usando PCA e PCA de kernel. Em seguida, plotamos as imagens reconstruídas para comparar os resultados.

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(
    kernel_pca.transform(X_test_noisy)
)
X_reconstructed_pca = pca.inverse_transform(pca.transform(X_test_noisy))

plot_digits(X_test, "Imagens de teste não corrompidas")
plot_digits(
    X_reconstructed_pca,
    f"Reconstrução PCA\nMSE: {np.mean((X_test - X_reconstructed_pca) ** 2):.2f}",
)
plot_digits(
    X_reconstructed_kernel_pca,
    (
        "Reconstrução PCA de Kernel\n"
        f"MSE: {np.mean((X_test - X_reconstructed_kernel_pca) ** 2):.2f}"
    ),
)
```
