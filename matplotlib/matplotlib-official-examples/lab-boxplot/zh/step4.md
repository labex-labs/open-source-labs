# 移除单个组件

我们可以使用`boxplot()`函数中可用的各种关键字参数来移除箱线图的单个组件。例如，我们可以通过将`showmeans`设置为`False`来移除均值。我们还可以分别通过将`showbox`和`showcaps`设置为`False`来移除箱体和须线。

```python
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), sharey=True)
axs[0, 0].boxplot(data, labels=labels)
axs[0, 0].set_title('Default')

axs[0, 1].boxplot(data, labels=labels, showmeans=False)
axs[0, 1].set_title('No Means')

axs[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)
axs[1, 0].set_title('No Box or Whiskers')

axs[1, 1].boxplot(data, labels=labels, showfliers=False)
axs[1, 1].set_title('No Outliers')

plt.show()
```
