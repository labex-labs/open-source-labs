# 重建并去噪测试图像

我们使用主成分分析（PCA）和核主成分分析（Kernel PCA）对有噪声的测试集进行变换和重建。然后我们绘制重建后的图像以比较结果。

```python
X_reconstructed_kernel_pca = kernel_pca.inverse_transform(
    kernel_pca.transform(X_test_noisy)
)
X_reconstructed_pca = pca.inverse_transform(pca.transform(X_test_noisy))

plot_digits(X_test, "未损坏的测试图像")
plot_digits(
    X_reconstructed_pca,
    f"PCA 重建\n均方误差（MSE）：{np.mean((X_test - X_reconstructed_pca) ** 2):.2f}",
)
plot_digits(
    X_reconstructed_kernel_pca,
    (
        "核主成分分析重建\n"
        f"均方误差（MSE）：{np.mean((X_test - X_reconstructed_kernel_pca) ** 2):.2f}"
    ),
)
```
