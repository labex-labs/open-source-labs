# 创建绘图

既然你已经生成了数据，接下来将使用 `imshow()` 函数创建绘图。

```python
fig, ax = plt.subplots()
im = ax.imshow(data2d)
ax.set_title('Pan on the colorbar to shift the color mapping\n'
             'Zoom on the colorbar to scale the color mapping')
```
