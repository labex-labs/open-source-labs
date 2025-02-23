# 矢印注釈を追加する

矢印を使って、グラフの特定の特徴や傾向を指摘することができます。このステップでは、最大値を指す矢印をグラフに追加します。

```python
# Find the maximum value
y = [0, 1, 4, 9, 16]
max_index = y.index(max(y))
xmax = max_index
ymax = y[max_index]

# Add arrow annotation
ax.annotate('Maximum Value', xy=(xmax, ymax), xytext=(xmax, ymax + 5),
            arrowprops=dict(facecolor='black', shrink=0.05))
plt.show()
```
