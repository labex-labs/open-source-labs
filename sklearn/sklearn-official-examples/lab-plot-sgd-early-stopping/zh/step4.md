# 绘制结果

最后一步是绘制结果。我们将使用两个子图来绘制训练分数和测试分数，以及迭代次数和拟合时间。对于每个估计器和停止标准，我们将使用不同的线条样式。

```python
# 定义要绘制的内容
lines = "停止标准"
x 轴 = "max_iter"
样式 = ["-.", "--", "-"]

# 第一个图：训练分数和测试分数
fig, axes = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12, 4))
for ax, y_axis in zip(axes, ["训练分数", "测试分数"]):
    for style, (标准, group_df) in zip(样式, results_df.groupby(lines)):
        group_df.plot(x=x 轴, y=y_axis, label=标准, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

# 第二个图：n_iter 和拟合时间
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 4))
for ax, y_axis in zip(axes, ["n_iter_", "拟合时间（秒）"]):
    for style, (标准, group_df) in zip(样式, results_df.groupby(lines)):
        group_df.plot(x=x 轴, y=y_axis, label=标准, ax=ax, style=style)
    ax.set_title(y_axis)
    ax.legend(title=lines)
fig.tight_layout()

plt.show()
```

需注意，这里代码中的中文部分是为了符合翻译要求对变量名进行的翻译，实际代码中变量名应为英文。
