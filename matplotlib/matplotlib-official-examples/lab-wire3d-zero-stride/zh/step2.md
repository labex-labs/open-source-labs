# 创建一个图形和两个子图

我们将使用 `subplots()` 方法创建一个带有两个子图的图形。我们还将投影设置为 `'3d'`，这样我们的子图将是三维的。

```python
fig, (ax1, ax2) = plt.subplots(
    2, 1, figsize=(8, 12), subplot_kw={'projection': '3d'})
```
