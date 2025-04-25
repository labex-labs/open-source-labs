# データセットの可視化

manifold.SpectralEmbedding() を使って手書き数字データセットの 2 次元埋め込みを計算し、各数字に異なるマーカーを付けた散布図を描画することで、データセットを可視化します。

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
    plt.title('Digits Dataset Scatter Plot', size=17)
    plt.axis("off")
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])

print("Computing embedding")
X_red = manifold.SpectralEmbedding(n_components=2).fit_transform(X)
print("Done.")
plot_dataset(X_red)
```
