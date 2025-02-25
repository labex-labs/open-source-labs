# 形状注釈を追加する

ここでは、グラフに形状注釈を追加します。次のコードでは、2 番目のデータポイントの周りに四角形を追加します。

```python
bbox = dict(boxstyle="round", fc="0.8")
ax.annotate("Data Point 2", xy=(2, 4), xytext=(2.5, 4.5),
            bbox=bbox,
            arrowprops=dict(facecolor="black", shrink=0.05))
```
