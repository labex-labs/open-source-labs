# 创建图形和子图

下一步是创建一个图形和子图。我们将使用`subplots`函数创建一个包含两个并排子图的图形。

```python
fig, (ax0, ax1) = plt.subplots(ncols=2, figsize=(7, 4))
```
