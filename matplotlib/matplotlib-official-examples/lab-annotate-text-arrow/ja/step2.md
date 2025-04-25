# グラフにテキスト注釈を追加する

次に、`ax.text()` 関数を使ってグラフにテキスト注釈を追加します。「サンプル A」用と「サンプル B」用の 2 つの注釈を作成します。

```python
bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Sample A", ha="center", va="center", size=20,
        bbox=bbox_props)
ax.text(2, 2, "Sample B", ha="center", va="center", size=20,
        bbox=bbox_props)
```
