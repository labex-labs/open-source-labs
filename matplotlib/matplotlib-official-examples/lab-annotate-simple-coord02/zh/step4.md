# 添加形状注释

形状可用于吸引对图表特定区域的关注。在这一步中，我们将添加一个矩形来突出显示\(x = 1\) 和\(x = 3\) 之间的区域。

```python
# 添加形状注释
ax.axvspan(1, 3, facecolor='gray', alpha=0.2)
plt.show()
```
