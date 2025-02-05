# 创建动画

最后，我们可以使用 `FuncAnimation` 类来创建动画。我们将传递 `fig`、`run`、`data_gen`、`init_func` 和 `interval` 参数来创建动画。我们还将设置 `save_count` 参数为 100，以确保只保存最后 100 帧。

```python
ani = animation.FuncAnimation(fig, run, data_gen, interval=100, init_func=init,
                              save_count=100)
```
