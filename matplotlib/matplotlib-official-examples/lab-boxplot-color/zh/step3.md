# 创建矩形箱线图

现在我们将使用 Matplotlib 中的 `boxplot()` 函数创建一个矩形箱线图。我们将把 `patch_artist` 参数设置为 `True` 以便用颜色填充箱体。

```python
fig, ax1 = plt.subplots(figsize=(9, 4))
bplot1 = ax1.boxplot(all_data,
                     vert=True,  # 垂直箱体对齐
                     patch_artist=True,  # 用颜色填充
                     labels=labels)  # x 轴刻度标签
ax1.set_title('Rectangular Box Plot')
```
