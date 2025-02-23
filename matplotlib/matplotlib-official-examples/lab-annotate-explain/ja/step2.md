# 矢印で 2 点を結ぶ

このステップでは、矢印で 2 点を結びます。矢印を作成するには `annotate` 関数を使い、矢印のスタイルと色をカスタマイズします。

```python
ax = axs.flat[0]
ax.plot([x1, x2], [y1, y2], ".")
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
