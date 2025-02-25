# コントアープロットの作成

次に、`contour()` 関数を使ってコントアープロットを作成します。`X`、`Y`、`Z` のデータを渡し、曲線を垂直方向に「リボン」に拡張するために `extend3d=True` を設定します。また、色付けを美しくするためにカラーマップを `cm.coolwarm` に設定します。

```python
ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)
```
