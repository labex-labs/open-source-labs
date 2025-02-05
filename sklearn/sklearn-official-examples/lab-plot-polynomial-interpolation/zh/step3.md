# B样条插值

我们将使用 `SplineTransformer` 来生成B样条基函数，并对训练数据拟合一个岭回归模型。然后，我们绘制函数、训练点以及使用B样条的插值。

```python
# 具有4 + 3 - 1 = 6个基函数的B样条
model = make_pipeline(SplineTransformer(n_knots=4, degree=3), Ridge(alpha=1e-3))
model.fit(X_train, y_train)

y_plot = model.predict(X_plot)
ax.plot(x_plot, y_plot, label="B-spline")
ax.legend(loc="lower center")
ax.set_ylim(-20, 10)
plt.show()
```
