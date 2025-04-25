# 自定义小提琴图外观

现在我们将自定义小提琴图的外观。首先，我们通过将`showmeans`、`showmedians`和`showextrema`参数设置为`False`来限制 Matplotlib 绘制的内容。然后，我们使用`set_facecolor`和`set_alpha`方法更改小提琴主体的颜色和透明度。最后，我们在小提琴图上方添加一个简化的箱线图表示，使用 NumPy 的`percentile`函数来计算四分位数、中位数和须线。

```python
# 自定义小提琴图外观
fig, ax2 = plt.subplots()
ax2.set_title('Customized Violin Plot')
ax2.set_ylabel('Observed Values')

# 创建小提琴图
parts = ax2.violinplot(
        data, showmeans=False, showmedians=False,
        showextrema=False)

# 自定义小提琴主体
for pc in parts['bodies']:
    pc.set_facecolor('#D43F3A')
    pc.set_edgecolor('black')
    pc.set_alpha(1)

# 添加箱线图
quartile1, medians, quartile3 = np.percentile(data, [25, 50, 75], axis=1)
whiskers = np.array([
    adjacent_values(sorted_array, q1, q3)
    for sorted_array, q1, q3 in zip(data, quartile1, quartile3)])
whiskers_min, whiskers_max = whiskers[:, 0], whiskers[:, 1]

inds = np.arange(1, len(medians) + 1)
ax2.scatter(inds, medians, marker='o', color='white', s=30, zorder=3)
ax2.vlines(inds, quartile1, quartile3, color='k', linestyle='-', lw=5)
ax2.vlines(inds, whiskers_min, whiskers_max, color='k', linestyle='-', lw=1)
```
