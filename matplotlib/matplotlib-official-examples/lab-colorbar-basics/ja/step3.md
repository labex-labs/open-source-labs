# 正のデータのプロットとカラーバーを作成する

正のデータのプロットを作成し、`colorbar` 関数を使ってプロットにカラーバーを追加します。

```python
# plot just the positive data and save the
# color "mappable" object returned by ax1.imshow
pos = plt.imshow(Zpos, cmap='Blues', interpolation='none')

# add the colorbar using the figure's method,
# telling which mappable we're talking about and
# which axes object it should be near
plt.colorbar(pos)
```
