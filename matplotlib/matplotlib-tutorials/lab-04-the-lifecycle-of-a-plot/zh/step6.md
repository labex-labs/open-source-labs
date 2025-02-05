# 组合多个可视化元素

我们可以向可视化图形中添加其他绘图元素。请按以下步骤操作：

1. 添加一条代表销售数据平均值的垂直线。

```python
ax.axvline(group_mean, ls='--', color='r')
```

2. 在图上标注新公司。

```python
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10, verticalalignment="center")
```

3. 调整绘图标题的位置。

```python
ax.title.set(y=1.05)
```

4. 完整代码如下所示。

```python
fig, ax = plt.subplots(figsize=(8, 8))
ax.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45, horizontalalignment='right')

# Add a vertical line, here we set the style in the function call
ax.axvline(group_mean, ls='--', color='r')

# Annotate new companies
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")

# Now we move our title up since it's getting a little cramped
ax.title.set(y=1.05)

ax.set(xlim=[-10000, 140000], xlabel='Total Revenue', ylabel='Company',
       title='Company Revenue')

plt.show()
```
