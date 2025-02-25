# ハッチ付きの楕円パッチを追加する

ハッチ付きのパッチをプロットに追加することもできます。この場合、add_patch 関数を使って楕円パッチをプロットに追加します。

```python
plt.gca().add_patch(Ellipse((4, 50), 10, 10, fill=True, hatch='*', facecolor='y'))
```
