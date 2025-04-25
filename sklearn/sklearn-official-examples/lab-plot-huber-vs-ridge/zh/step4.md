# 可视化数据集

我们现在将使用 matplotlib 可视化数据集。我们将绘制 X 的值与 y 的值的关系图。

```python
plt.plot(X, y, "b.")
plt.title("Dataset with Strong Outliers")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
