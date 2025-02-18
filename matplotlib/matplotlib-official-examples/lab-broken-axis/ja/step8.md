# 切り抜き斜線を作成する

最後に、切り抜き斜線を作成します。軸座標で線オブジェクトを作成し、`ax1.transAxes` と `ax2.transAxes` を使用して各サブプロットの座標に変換します。`ax1.plot` と `ax2.plot` を使用して線をプロットします。また、`marker` でマーカーのスタイルを指定し、`markersize` でマーカーのサイズを設定し、`linestyle` で線のスタイルを設定し、`color` で線の色を設定し、`mec` でマーカーの枠線の色を設定し、`mew` でマーカーの枠線の幅を設定します。

```python
d =.5
kwargs = dict(marker=[(-1, -d), (1, d)], markersize=12,
              linestyle="none", color='k', mec='k', mew=1, clip_on=False)
ax1.plot([0, 1], [0, 0], transform=ax1.transAxes, **kwargs)
ax2.plot([0, 1], [1, 1], transform=ax2.transAxes, **kwargs)
```
