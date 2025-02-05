# 自定义箱线图样式

我们还可以使用`boxplot()`函数中可用的各种关键字参数来自定义箱线图的样式。例如，我们可以通过设置`boxprops`来更改箱体的颜色和线条样式。我们还可以分别通过设置`medianprops`、`meanprops`和`meanlineprops`来更改中位数、均值和均值线的样式。

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

boxprops = dict(linestyle='--', linewidth=2, color='red')
axs[0, 1].boxplot(data, labels=labels, boxprops=boxprops)
axs[0, 1].set_title('Custom Box')

medianprops = dict(linestyle='-', linewidth=2, color='blue')
meanprops = dict(marker='D', markeredgecolor='black', markerfacecolor='green')
meanlineprops = dict(linestyle='--', linewidth=2, color='red')
axs[1, 0].boxplot(data, labels=labels, medianprops=medianprops, meanprops=meanprops, meanline=True, meanlineprops=meanlineprops)
axs[1, 0].set_title('Custom Median, Mean, and Mean Line')

flierprops = dict(marker='o', markerfacecolor='red', markersize=8, markeredgecolor='none')
axs[1, 1].boxplot(data, labels=labels, flierprops=flierprops)
axs[1, 1].set_title('Custom Outliers')

plt.show()
```
