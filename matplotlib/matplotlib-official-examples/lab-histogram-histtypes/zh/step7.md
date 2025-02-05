# 创建两个堆叠柱状图的直方图

我们可以通过调用两次 `hist` 函数并将 `histtype` 参数设置为 `'barstacked'` 来创建两个堆叠柱状图的直方图。在这个例子中，我们将创建两个堆叠柱状图的直方图。

```python
plt.hist(x, density=True, histtype='barstacked', rwidth=0.8)
plt.hist(w, density=True, histtype='barstacked', rwidth=0.8)
plt.show()
```
