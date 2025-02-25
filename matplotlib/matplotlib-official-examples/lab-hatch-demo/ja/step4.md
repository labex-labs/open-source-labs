# 複数のハッチ付きの棒グラフを作成する

棒グラフでは複数のハッチを使うこともできます。この場合、ハッチの配列を使って棒に複数のハッチを作成します。

```python
plt.bar(x, y1, edgecolor='black', hatch=['--', '+', 'x', '\\'])
plt.bar(x, y2, bottom=y1, edgecolor='black', hatch=['*', 'o', 'O', '.'])
```
