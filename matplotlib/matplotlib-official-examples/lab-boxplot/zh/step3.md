# 默认箱线图

我们将首先创建一个默认箱线图来可视化数据。我们会使用 Matplotlib 函数`boxplot()`，并将数据和标签作为参数传入。我们还会使用`set_title()`函数设置图表的标题。

```python
fig, ax = plt.subplots()
ax.boxplot(data, labels=labels)
ax.set_title('Default Box Plot')
plt.show()
```
