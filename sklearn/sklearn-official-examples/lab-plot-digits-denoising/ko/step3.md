# 테스트 이미지 플롯

테스트 이미지를 플롯하는 도우미 함수를 정의합니다. 이 함수를 사용하여 손상되지 않은 테스트 이미지와 잡음이 있는 테스트 이미지를 플롯합니다.

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
