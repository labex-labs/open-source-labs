# 创建 “下一个” 和 “上一个” 按钮

现在，我们将使用 `matplotlib.pyplot` 的 `add_axes` 函数创建 “下一个” 和 “上一个” 按钮，并使用 `on_clicked` 将我们之前创建的回调函数分配给它们。

```python
axprev = fig.add_axes([0.7, 0.05, 0.1, 0.075])
axnext = fig.add_axes([0.81, 0.05, 0.1, 0.075])
bnext = Button(axnext, 'Next')
bnext.on_clicked(callback.next)
bprev = Button(axprev, 'Previous')
bprev.on_clicked(callback.prev)
```
