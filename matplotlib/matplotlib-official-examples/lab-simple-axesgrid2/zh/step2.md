# 创建一个图形和图像网格

接下来，我们使用 `nrows_ncols` 参数创建一个图形和图像网格，以定义网格的行数和列数。

```python
fig = plt.figure(figsize=(5.5, 3.5))
grid = ImageGrid(fig, 111,  # 类似于 subplot(111)
                 nrows_ncols=(1, 3),
                 axes_pad=0.1,
                 label_mode="L")
```
