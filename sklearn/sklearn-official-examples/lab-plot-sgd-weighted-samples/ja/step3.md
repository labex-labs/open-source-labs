# 重み付きデータセットをプロットする

matplotlib ライブラリを使って重み付きデータセットをプロットします。点のサイズはその重みに比例します。

```python
xx, yy = np.meshgrid(np.linspace(-4, 5, 500), np.linspace(-4, 5, 500))
fig, ax = plt.subplots()
ax.scatter(
    X[:, 0],
    X[:, 1],
    c=y,
    s=sample_weight,
    alpha=0.9,
    cmap=plt.cm.bone,
    edgecolor="black",
)
```
