# パワー法則正規化の作成

このステップでは、異なるガンマ値でパワー法則正規化を作成する必要があります。

```python
for ax, gamma in zip(axs.flat[1:], gammas):
    ax.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
