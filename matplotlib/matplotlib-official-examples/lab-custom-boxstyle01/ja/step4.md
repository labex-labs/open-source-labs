# カスタムボックススタイルを使用する

カスタムボックススタイルを実装して登録したら、`Axes.text` で使用できます。

```python
fig, ax = plt.subplots(figsize=(3, 3))
ax.text(0.5, 0.5, "Test", size=30, va="center", ha="center", rotation=30,
        bbox=dict(boxstyle="angled,pad=0.5", alpha=0.2))
```
