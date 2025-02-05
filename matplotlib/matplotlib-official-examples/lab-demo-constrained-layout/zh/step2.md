# 定义示例绘图

我们定义一个函数，该函数创建一个带有x轴和y轴标签以及标题的简单折线图。

```python
def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel('x-label', fontsize=12)
    ax.set_ylabel('y-label', fontsize=12)
    ax.set_title('Title', fontsize=14)
```
