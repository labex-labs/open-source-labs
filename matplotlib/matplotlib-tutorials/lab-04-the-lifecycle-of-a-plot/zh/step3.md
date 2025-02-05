# 创建绘图

我们将使用条形图可视化来展示销售数据。请按以下步骤操作：

1. 使用 `plt.subplots()` 创建一个图形和一个轴对象。

```python
fig, ax = plt.subplots()
```

2. 使用轴对象的 `barh()` 方法绘制数据。

```python
ax.barh(group_names, group_data)
```
