# 重みの可視化

最後に、MLP の最初の層の重みを可視化します。4x4 のサブプロットのグリッドを作成し、各重みを 28x28 ピクセルのグレースケール画像として表示します。

```python
fig, axes = plt.subplots(4, 4)
vmin, vmax = mlp.coefs_[0].min(), mlp.coefs_[0].max()
for coef, ax in zip(mlp.coefs_[0].T, axes.ravel()):
    ax.matshow(coef.reshape(28, 28), cmap=plt.cm.gray, vmin=0.5 * vmin, vmax=0.5 * vmax)
    ax.set_xticks(())
    ax.set_yticks(())

plt.show()
```
