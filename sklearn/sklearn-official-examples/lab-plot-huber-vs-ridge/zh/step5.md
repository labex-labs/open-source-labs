# 拟合 Huber 回归器

我们现在将把 HuberRegressor 拟合到数据集上。我们将在一系列 epsilon 值上拟合模型，以展示随着 epsilon 值的增加，决策函数如何趋近于岭回归（Ridge regression）的决策函数。

```python
# 定义 epsilon 值的范围
epsilon_values = [1, 1.5, 1.75, 1.9]

# 定义用于绘图的 x 值
x = np.linspace(X.min(), X.max(), 7)

# 定义用于绘图的颜色
colors = ["r-", "b-", "y-", "m-"]

# 在一系列 epsilon 值上拟合 Huber 回归器。
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
