# ヒストグラムのカスタマイズ

2 次元ヒストグラムをカスタマイズするのは 1 次元の場合と同様で、ビンのサイズや色の正規化などの視覚的なコンポーネントを制御できます。

```python
fig, axs = plt.subplots(3, 1, figsize=(5, 15), sharex=True, sharey=True,
                        tight_layout=True)

# 各軸のビンの数を増やすことができます
axs[0].hist2d(dist1, dist2, bins=40)

# 色の正規化も定義できます
axs[1].hist2d(dist1, dist2, bins=40, norm=colors.LogNorm())

# 各軸のカスタムなビンの数も定義できます
axs[2].hist2d(dist1, dist2, bins=(80, 10), norm=colors.LogNorm())

plt.show()
```
