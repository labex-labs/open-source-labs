# 为图表添加注释

现在，我们将通过添加一个指向特定坐标的箭头来为图表添加注释。在这个例子中，我们将添加一个指向余弦函数局部最大值的箭头。

```python
ax.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
            arrowprops=dict(facecolor='black', shrink=0.05),
            )
```

`ax.annotate()` 函数接受几个参数。第一个参数是将显示在图表上的文本。`xy` 参数指定我们要注释的点的坐标。`xytext` 参数指定文本的坐标。`arrowprops` 参数是一个字典，用于指定箭头的属性。
