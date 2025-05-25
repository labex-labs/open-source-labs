# 데이터셋 시각화

manifold.SpectralEmbedding() 을 사용하여 숫자 데이터셋의 2 차원 임베딩을 계산하고 각 숫자에 대해 다른 마커로 산점도를 플롯하여 데이터셋을 시각화합니다.

```python
def plot_dataset(X_red):
    x_min, x_max = np.min(X_red, axis=0), np.max(X_red, axis=0)
    X_red = (X_red - x_min) / (x_max - x_min)

    plt.figure(figsize=(6, 4))
    for digit in digits.target_names:
        plt.scatter(
            *X_red[y == digit].T,
            marker=f"${digit}$",
            s=50,
            alpha=0.5,
        )

    plt.xticks([])
    plt.yticks([])
    plt.title('숫자 데이터셋 산점도', size=17)
    plt.axis("off")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

print("임베딩 계산 중")
X_red = manifold.SpectralEmbedding(n_components=2).fit_transform(X)
print("완료.")
plot_dataset(X_red)
```
