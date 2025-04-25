# 自定义绘图外观

我们可以进一步自定义绘图的外观。请按以下步骤操作：

1. 旋转 x 轴标签，使其更具可读性。

```python
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
```

2. 设置 x 轴和 y 轴的范围、标签以及标题。

```python
ax.set(xlim=[-10000, 140000],
       xlabel='Total Revenue',
       ylabel='Company',
       title='Company Revenue')
```

3. 再次显示绘图。

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')
ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')
```
