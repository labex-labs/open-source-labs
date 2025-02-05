# 创建默认小提琴图

接下来，我们将使用Matplotlib的`violinplot`函数创建一个默认的小提琴图。这将为我们在后续步骤中自定义图表时提供一个比较的基准。

```python
# 创建默认小提琴图
fig, ax1 = plt.subplots()
ax1.set_title('Default Violin Plot')
ax1.set_ylabel('Observed Values')
ax1.violinplot(data)
```
