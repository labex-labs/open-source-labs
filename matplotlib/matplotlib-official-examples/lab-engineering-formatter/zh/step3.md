# 创建图形和子图

我们需要创建一个图形和子图来显示数据。在本实验中，我们将并排创建两个子图。

```python
# Figure width is doubled (2*6.4) to display nicely 2 subplots side by side.
fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(7, 9.6))
for ax in (ax0, ax1):
    ax.set_xscale('log')
```
