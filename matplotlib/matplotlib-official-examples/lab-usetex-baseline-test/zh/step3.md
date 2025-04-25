# 创建子图

我们将创建一个包含两个子图的图形，一个使用数学文本（mathtext），另一个使用 TeX（usetex）。我们将使用 `subplots()` 方法来创建子图。

```python
fig, axs = plt.subplots(1, 2, figsize=(2 * 3, 6.5))
```
