# 切换不同元素的显示

我们可以使用 `bxp()` 函数中的各种参数来切换箱线图不同元素的显示。在这个例子中，我们展示如何显示或隐藏均值、箱体、箱须、凹口和异常值。

```python
# Toggle the display of different elements
plt.bxp(stats, showmeans=True, showbox=False, showcaps=False, shownotches=True, showfliers=False)
plt.show()
```
