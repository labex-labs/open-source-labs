# パワー法則正規化の作成

このステップでは、`PowerNorm()` を使用してパワー法則正規化を作成する必要があります。

```python
plt.hist2d(data[:, 0], data[:, 1], bins=100, norm=mcolors.PowerNorm(gamma))
```
