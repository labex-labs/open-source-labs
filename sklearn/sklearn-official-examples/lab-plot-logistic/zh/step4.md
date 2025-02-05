# 绘制结果

最后一步是绘制结果。我们将使用 `matplotlib` 创建示例数据的散点图，并绘制逻辑回归模型和线性回归模型。

```python
# 并绘制结果
plt.figure(1, figsize=(4, 3))
plt.clf()
plt.scatter(X.ravel(), y, label="示例数据", color="黑色", zorder=20)
X_test = np.linspace(-5, 10, 300)

损失 = expit(X_test * clf.coef_ + clf.intercept_).ravel()
plt.plot(X_test, 损失, label="逻辑回归模型", color="红色", linewidth=3)

ols = LinearRegression()
ols.fit(X, y)
plt.plot(
    X_test,
    ols.coef_ * X_test + ols.intercept_,
    label="线性回归模型",
    linewidth=1,
)
plt.axhline(0.5, color=".5")

plt.ylabel("y")
plt.xlabel("X")
plt.xticks(range(-5, 10))
plt.yticks([0, 0.5, 1])
plt.ylim(-0.25, 1.25)
plt.xlim(-4, 10)
plt.legend(
    loc="lower right",
    fontsize="small",
)
plt.tight_layout()
plt.show()
```
