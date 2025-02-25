# 矢印注釈を追加する

ここでは、グラフに矢印注釈を追加します。次のコードでは、最初のデータポイントから 2 番目のデータポイントに矢印を追加します。

```python
ax.annotate("", xy=(1, 3), xytext=(2, 4),
            arrowprops=dict(arrowstyle="->", connectionstyle="arc3"))
```
