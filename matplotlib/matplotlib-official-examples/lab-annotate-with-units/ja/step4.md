# 単位付きのxy座標とテキストで矢印注釈を追加する

このステップでは、`annotate()`関数を使ってプロットに矢印注釈を追加します。矢印の位置、表示するテキスト、および矢印のプロパティを指定します。また、位置とテキストの測定単位も指定します。

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8*cm, 0.95*cm), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
