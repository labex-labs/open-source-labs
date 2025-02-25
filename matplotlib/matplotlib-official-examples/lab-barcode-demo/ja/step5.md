# バーコードを描画する

最後に、`Axes.imshow` を使ってバーコードを描画できます。データを 1 行の 2 次元配列に変換するために `code.reshape(1, -1)` を使い、非正方形のピクセルを許容するために `imshow(..., aspect='auto')` を使い、ぼかしたエッジを防ぐために `imshow(..., interpolation='nearest')` を使います。

```python
ax.imshow(code.reshape(1, -1), cmap='binary', aspect='auto',
          interpolation='nearest')
plt.show()
```
