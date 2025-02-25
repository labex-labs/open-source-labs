# 注釈の配置

異なる座標系を使って注釈の配置を行うことができます。次のコードでは、データ座標を使ってテキスト注釈を配置し、グラフ座標を使って矢印注釈を配置します。

```python
ax.annotate("Data Point 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="data")
ax.annotate("", xy=(1, 3), xytext=(0.5, 0.5),
            arrowprops=dict(facecolor="black", shrink=0.05),
            xycoords="data", textcoords="figure fraction")
```
