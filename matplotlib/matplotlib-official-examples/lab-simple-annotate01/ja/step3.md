# テキスト注釈を追加する

ここでは、グラフにテキスト注釈を追加します。次のコードでは、最初のデータポイントに「Data Point 1」というテキストを追加します。

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05))
```
