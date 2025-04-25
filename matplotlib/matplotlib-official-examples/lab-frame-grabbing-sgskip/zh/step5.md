# 获取帧并写入文件

我们进行 100 次迭代循环，为 x 和 y 坐标生成随机数。我们更新线图的数据，并使用写入器获取帧。最后，我们将帧保存到一个文件中。

```python
x0, y0 = 0, 0

with writer.saving(fig, "writer_test.mp4", 100):
    for i in range(100):
        x0 += 0.1 * np.random.randn()
        y0 += 0.1 * np.random.randn()
        l.set_data(x0, y0)
        writer.grab_frame()
```
