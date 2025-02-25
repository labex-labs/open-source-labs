# ハッチ付きのパッチを持つプロットを作成する

プロットではパッチにハッチを使うこともできます。この場合、fill_between 関数を使ってハッチ付きのパッチを作成します。

```python
x = np.arange(0, 40, 0.2)
plt.fill_between(x, np.sin(x) * 4 + 30, y2=0, hatch='///', zorder=2, fc='c')
```
