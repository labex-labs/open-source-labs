# 绘制测试图像

我们定义一个辅助函数来绘制测试图像。我们使用这个函数来绘制未损坏的和有噪声的测试图像。

```python
import matplotlib.pyplot as plt

def plot_digits(X, title):
    fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(8, 8))
    for img, ax in zip(X, axs.ravel()):
        ax.imshow(img.reshape((16, 16)), cmap="Greys")
        ax.axis("off")
    fig.suptitle(title, fontsize=24)

plot_digits(X_test, "未损坏的测试图像")
plot_digits(
    X_test_noisy, f"有噪声的测试图像\n均方误差（MSE）：{np.mean((X_test - X_test_noisy) ** 2):.2f}"
)
```
