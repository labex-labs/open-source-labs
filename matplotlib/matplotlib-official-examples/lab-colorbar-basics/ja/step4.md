# 負のデータのプロットとカラーバーを作成する

負のデータのプロットを作成し、`colorbar` 関数を使ってプロットにカラーバーを追加します。今回は、カラーバーの位置と、アンカーと縮小パラメータを指定します。

```python
# repeat everything above for the negative data
# you can specify location, anchor and shrink the colorbar
neg = plt.imshow(Zneg, cmap='Reds_r', interpolation='none')
plt.colorbar(neg, location='right', anchor=(0, 0.3), shrink=0.7)
```
