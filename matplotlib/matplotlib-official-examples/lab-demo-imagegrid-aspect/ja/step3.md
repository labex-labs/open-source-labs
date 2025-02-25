# 画像グリッドを作成する

画像を表示するために2つの画像グリッドを作成します。最初の画像グリッドは2行2列、2番目の画像グリッドも2行2列になります。

```python
grid1 = ImageGrid(fig, 121, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
grid2 = ImageGrid(fig, 122, (2, 2), axes_pad=0.1, aspect=True, share_all=True)
```
