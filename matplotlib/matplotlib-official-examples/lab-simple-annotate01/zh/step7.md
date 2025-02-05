# 放置注释

我们可以使用不同的坐标系来放置注释。以下代码将使用数据坐标放置文本注释，并使用图形坐标放置箭头注释。

```python
ax.annotate("数据点 1", xy=(1, 3), xytext=(1.5, 3.5),
            arrowprops=dict(facecolor="黑色", shrink=0.05),
            xycoords="data", textcoords="data")
ax.annotate("", xy=(1, 3), xytext=(0.5, 0.5),
            arrowprops=dict(facecolor="黑色", shrink=0.05),
            xycoords="data", textcoords="figure fraction")
```
