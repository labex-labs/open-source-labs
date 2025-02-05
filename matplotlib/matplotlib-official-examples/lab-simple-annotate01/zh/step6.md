# 自定义注释

我们可以通过更改字体大小、字体颜色和箭头样式来自定义注释。以下代码将更改文本注释的字体大小、字体颜色和箭头样式。

```python
ax.annotate("数据点 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="黑色", shrink=0.05, arrowstyle="->"),
            fontsize=12, color="红色")
```
