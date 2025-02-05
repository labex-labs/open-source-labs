# 添加混合单位的箭头注释

在这一步中，我们将使用 `annotate()` 函数向绘图添加另一个箭头注释。我们将提供箭头的位置、要显示的文本以及箭头属性。我们还将在位置上混合使用不同的度量单位，并在文本中使用轴比例。

```python
ax.annotate('local max', xy=(3*cm, 1*cm), xycoords='data',
            xytext=(0.8, 0.95), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            horizontalalignment='right', verticalalignment='top')
```
