# 添加带有单位化 xy 和文本的箭头注释

在这一步中，我们将使用 `annotate()` 函数向绘图添加一个箭头注释。我们将提供箭头的位置、要显示的文本以及箭头属性。我们还将指定位置和文本的度量单位。

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8*cm, 0.95*cm), textcoords='data',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
