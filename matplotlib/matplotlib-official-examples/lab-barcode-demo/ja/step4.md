# グラフと軸を作成する

バーコード用のグラフと軸を作成する必要があります。グラフのサイズをデータポイントの数の倍数に設定し、すべての軸を非表示にします。

```python
fig = plt.figure(figsize=(len(code) * pixel_per_bar / dpi, 2), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])  # span the whole figure
ax.set_axis_off()
```
