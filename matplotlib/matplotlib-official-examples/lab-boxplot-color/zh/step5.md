# 用自定义颜色填充箱线图

接下来，我们将用自定义颜色填充箱线图。我们将创建一个颜色列表，并使用循环为每个箱体填充不同的颜色。

```python
colors = ['pink', 'lightblue', 'lightgreen']
for bplot in (bplot1, bplot2):
    for patch, color in zip(bplot['boxes'], colors):
        patch.set_facecolor(color)
```
