# 创建动画函数

我们需要创建一个 `animate` 函数，该函数生成新的随机数据并更新矩形的高度。

```python
def animate(frame_number):
    # simulate new data coming in
    data = np.random.randn(1000)
    n, _ = np.histogram(data, HIST_BINS)
    for count, rect in zip(n, bar_container.patches):
        rect.set_height(count)
    return bar_container.patches
```
