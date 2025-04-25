# 図形注釈を追加する

図形を使って、グラフの特定の領域に注目を集めることができます。このステップでは、x = 1 と x = 3 の間の領域を強調するために矩形を追加します。

```python
# Add shape annotation
ax.axvspan(1, 3, facecolor='gray', alpha=0.2)
plt.show()
```
