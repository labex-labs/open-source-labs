# Построение графиков тестовых изображений

Мы определяем вспомогательную функцию для построения графиков тестовых изображений. Мы используем эту функцию для построения графиков не искаженных и шумных тестовых изображений.

```python
import matplotlib.pyplot as plt

def plot_digits(X, title):
    fig, axs = plt.subplots(nrows=10, ncols=10, figsize=(8, 8))
    for img, ax in zip(X, axs.ravel()):
        ax.imshow(img.reshape((16, 16)), cmap="Greys")
        ax.axis("off")
    fig.suptitle(title, fontsize=24)

plot_digits(X_test, "Uncorrupted test images")
plot_digits(
    X_test_noisy, f"Noisy test images\nMSE: {np.mean((X_test - X_test_noisy) ** 2):.2f}"
)
```
