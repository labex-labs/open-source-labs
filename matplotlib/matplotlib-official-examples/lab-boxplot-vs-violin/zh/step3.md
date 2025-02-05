# 创建小提琴图

我们将使用 `violinplot()` 方法创建一个小提琴图。此方法接受多个参数，如数据、是否显示均值、是否显示中位数等。

```python
fig, axs = plt.subplots(nrows=1, ncols=2, figsize=(9, 4))
axs[0].violinplot(all_data, showmeans=False, showmedians=True)
axs[0].set_title('Violin plot')
```
