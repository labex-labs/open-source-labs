# 绘制结果

我们现在将绘制每种不同情况的结果。

```python
for title, this_X, this_y in [
    ("仅建模误差", X, y),
    ("X 数据损坏，小偏差", X_errors, y),
    ("y 数据损坏，小偏差", X, y_errors),
    ("X 数据损坏，大偏差", X_errors_large, y),
    ("y 数据损坏，大偏差", X, y_errors_large),
]:
    plt.figure(figsize=(5, 4))
    plt.plot(this_X[:, 0], this_y, "b+")

    for name, estimator in estimators:
        model = make_pipeline(PolynomialFeatures(3), estimator)
        model.fit(this_X, this_y)
        mse = mean_squared_error(model.predict(X_test), y_test)
        y_plot = model.predict(x_plot[:, np.newaxis])
        plt.plot(
            x_plot,
            y_plot,
            color=colors[name],
            linestyle=linestyle[name],
            linewidth=lw,
            label="%s: 误差 = %.3f" % (name, mse),
        )

    legend_title = "与未损坏数据的\n中位数绝对偏差误差"
    legend = plt.legend(
        loc="upper right", frameon=False, title=legend_title, prop=dict(size="x-small")
    )
    plt.xlim(-4, 10.2)
    plt.ylim(-2, 10.2)
    plt.title(title)
plt.show()
```
