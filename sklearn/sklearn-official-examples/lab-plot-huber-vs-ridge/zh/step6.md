# 拟合岭回归器

我们现在将把岭回归器（Ridge regressor）拟合到数据集上，并将其性能与 HuberRegressor 的性能进行比较。

```python
# 拟合一个岭回归器以与 Huber 回归器进行比较。
ridge = Ridge(alpha=0.0, random_state=0)
ridge.fit(X, y)
coef_ridge = ridge.coef_
coef_ = ridge.coef_ * x + ridge.intercept_
plt.plot(x, coef_, "g-", label="ridge regression")

# 给图添加图例
plt.legend(loc=0)

# 显示图形
plt.title("Comparison of HuberRegressor vs Ridge")
plt.xlabel("X")
plt.ylabel("y")
plt.show()
```
