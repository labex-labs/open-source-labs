# グラフに注釈を追加する

`ax.annotate()` 関数を使って、グラフに注釈を追加することができます。この関数は 3 つの引数を取ります：注釈のテキスト、注釈する点の xy 座標、およびテキスト位置の xy 座標。`arrowprops` 引数を使って、注釈のスタイルをカスタマイズできます。

```python
ax.annotate('annotate', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=0.05))
```
