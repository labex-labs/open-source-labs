# 应用该函数

既然我们已经有了这些函数，就可以用它们来创建一个带注释的热图。我们创建一组新的数据，为 `imshow` 提供更多参数，在注释上使用整数格式，并提供一些颜色。我们还通过使用 `matplotlib.ticker.FuncFormatter` 隐藏对角线元素（这些元素都是 1）。

```python
data = np.random.randint(2, 100, size=(7, 7))
y = [f"Book {i}" for i in range(1, 8)]
x = [f"Store {i}" for i in list("ABCDEFG")]

fig, ax = plt.subplots()
im, _ = heatmap(data, y, x, ax=ax, vmin=0, cmap="magma_r", cbarlabel="weekly sold copies")
annotate_heatmap(im, valfmt="{x:d}", size=7, threshold=20, textcolors=("red", "white"))

def func(x, pos):
    return f"{x:.2f}".replace("0.", ".").replace("1.00", "")

annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)
```
