# 楕円に接続する矢印をカスタマイズする

このステップでは、楕円に接続する矢印をカスタマイズします。矢印が楕円に接続するように `arrowprops` パラメータを使って指定し、矢印のスタイルと色もカスタマイズします。

```python
ax = axs.flat[2]
ax.plot([x1, x2], [y1, y2], ".")
el = mpatches.Ellipse((x1, y1), 0.3, 0.4, angle=30, alpha=0.2)
ax.add_artist(el)
ax.annotate("",
            xy=(x1, y1), xycoords='data',
            xytext=(x2, y2), textcoords='data',
            arrowprops=dict(arrowstyle="-",
                            color="0.5",
                            patchB=el,
                            connectionstyle="arc3,rad=0.3",
                            ),
            )
```
