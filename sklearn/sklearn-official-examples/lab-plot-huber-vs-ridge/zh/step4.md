# 可视化数据集

我们现在将使用matplotlib可视化数据集。我们将绘制X的值与y的值的关系图。

```python
plt.plot(X, y, "b.")
plt.title("Dataset with Strong Outliers")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
