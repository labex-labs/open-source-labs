# 混合単位で矢印注釈を追加する

このステップでは、`annotate()`関数を使ってプロットにもう 1 つの矢印注釈を追加します。矢印の位置、表示するテキスト、および矢印のプロパティを指定します。また、位置の測定単位を混合し、テキストにはグラフ座標系の割合を使用します。

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
