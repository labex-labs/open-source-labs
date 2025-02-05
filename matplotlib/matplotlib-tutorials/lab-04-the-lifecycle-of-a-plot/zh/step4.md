# 自定义绘图样式

我们可以更改绘图的样式，使其在视觉上更具吸引力。请按以下步骤操作：

1. 使用 `print(plt.style.available)` 打印可用样式列表。

```python
print(plt.style.available)
```

2. 选择一种样式并使用 `plt.style.use(style_name)` 应用它。

```python
plt.style.use('fivethirtyeight')
```

3. 让我们再次显示绘图。

```python
fig, ax = plt.subplots()
ax.barh(group_names, group_data)
```
