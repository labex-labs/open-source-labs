# 创建子图

接下来，我们使用 `plt.subplot_mosaic` 创建子图。我们将创建一个 3x2 的子图网格，并按如下方式为它们标注：

- 左上角的子图将标注为“a)”
- 左下角的子图将标注为“b)”
- 右上角和右下角的子图将分别标注为“c)”和“d)”

```python
fig, axs = plt.subplot_mosaic([['a)', 'c)'], ['b)', 'c)'], ['d)', 'd)']], layout='constrained')
```
