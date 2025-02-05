# 创建子图并调用 `test_rotation_mode` 函数

我们将创建两个子图，并使用 `fig` 和 `mode` 参数调用 `test_rotation_mode` 函数。

```python
fig = plt.figure(figsize=(8, 5))
subfigs = fig.subfigures(1, 2)
test_rotation_mode(subfigs[0], "default")
test_rotation_mode(subfigs[1], "anchor")
plt.show()
```
