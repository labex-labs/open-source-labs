# 创建绘图和图像

接下来，我们将创建一个绘图和一幅图像，以展示如何使用内嵌轴添加色条。

```python
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=[6, 3])

im1 = ax1.imshow([[1, 2], [2, 3]])
im2 = ax2.imshow([[1, 2], [2, 3]])
```
