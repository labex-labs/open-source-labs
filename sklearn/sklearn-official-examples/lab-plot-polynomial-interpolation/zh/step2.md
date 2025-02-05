# 多项式特征插值

我们将使用 `PolynomialFeatures` 来生成多项式特征，并对训练数据拟合一个岭回归模型。然后，我们绘制函数、训练点以及使用多项式特征的插值。

```python
# 绘制函数
lw = 2
fig, ax = plt.subplots()
ax.set_prop_cycle(
    color=["black", "teal", "yellowgreen", "gold", "darkorange", "tomato"]
)
ax.plot(x_plot, f(x_plot), linewidth=lw, label="ground truth")

# 绘制训练点
ax.scatter(x_train, y_train, label="training points")

# 多项式特征
for degree in [3, 4, 5]:
    model = make_pipeline(PolynomialFeatures(degree), Ridge(alpha=1e-3))
    model.fit(X_train, y_train)
    y_plot = model.predict(X_plot)
    ax.plot(x_plot, y_plot, label=f"degree {degree}")

ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```
