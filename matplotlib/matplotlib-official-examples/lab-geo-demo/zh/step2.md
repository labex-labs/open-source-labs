# 创建图形和子图

在这一步中，我们将为要创建的每个投影创建一个图形和四个子图。我们将使用 `plt.subplots()` 方法来创建图形和子图。

```python
fig, axs = plt.subplots(nrows=2, ncols=2, subplot_kw={'projection': 'aitoff'})
```
