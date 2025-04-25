# 画像グリッドを作成する

画像を表示するために 2 つの画像グリッドを作成します。最初の画像グリッドは 2 行 2 列、2 番目の画像グリッドも 2 行 2 列になります。

```python
grid1 = ImageGrid(fig, 121, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
grid2 = ImageGrid(fig, 122, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
```
