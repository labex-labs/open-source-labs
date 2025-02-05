# 拟合Huber回归器

我们现在将把HuberRegressor拟合到数据集上。我们将在一系列epsilon值上拟合模型，以展示随着epsilon值的增加，决策函数如何趋近于岭回归（Ridge regression）的决策函数。

```python
# 定义epsilon值的范围
epsilon_values = [1, 1.5, 1.75, 1.9]

# 定义用于绘图的x值
x = np.linspace(X.min(), X.max(), 7)

# 定义用于绘图的颜色
colors = ["r-", "b-", "y-", "m-"]

# 在一系列epsilon值上拟合Huber回归器。
for k, epsilon in enumerate(epsilon_values):
    huber = HuberRegressor(alpha=0.0, epsilon=epsilon)
    huber.fit(X, y)
    coef_ = huber.coef_ * x + huber.intercept_
    plt.plot(x, coef_, colors[k], label="huber loss, %s" % epsilon)

# 给图添加图例
plt.legend(loc=0)

# 显示图形
plt.title("HuberRegressor with Different Epsilon Values")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
