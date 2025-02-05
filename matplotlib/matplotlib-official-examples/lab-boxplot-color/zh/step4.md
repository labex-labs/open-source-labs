# 创建带缺口的箱线图

现在我们将使用 `boxplot()` 函数创建一个带缺口的箱线图。我们将把 `notch` 参数设置为 `True` 来创建带缺口的箱线图。

```python
fig, ax2 = plt.subplots(figsize=(9, 4))
bplot2 = ax2.boxplot(all_data,
                     notch=True,  # 缺口形状
                     vert=True,  # 垂直箱体对齐
                     patch_artist=True,  # 用颜色填充
                     labels=labels)  # x 轴刻度标签
ax2.set_title('Notched Box Plot')
```
