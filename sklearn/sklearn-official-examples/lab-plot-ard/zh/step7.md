# 绘制带有分数标准误差的多项式回归

误差线表示查询点预测高斯分布的一个标准差。请注意，在两个模型中使用默认参数时，ARD 回归最能捕捉到真实情况，但进一步减小贝叶斯岭的`lambda_init`超参数可以减少其偏差。最后，由于多项式回归的固有局限性，两个模型在外推时都会失败。

```python
ax = sns.scatterplot(
    data=full_data, x="input_feature", y="target", color="black", alpha=0.75
)
ax.plot(X_plot, y_plot, color="black", label="Ground Truth")
ax.plot(X_plot, y_brr, color="red", label="BayesianRidge with polynomial features")
ax.plot(X_plot, y_ard, color="navy", label="ARD with polynomial features")
ax.fill_between(
    X_plot.ravel(),
    y_ard - y_ard_std,
    y_ard + y_ard_std,
    color="navy",
    alpha=0.3,
)
ax.fill_between(
    X_plot.ravel(),
    y_brr - y_brr_std,
    y_brr + y_brr_std,
    color="red",
    alpha=0.3,
)
ax.legend()
_ = ax.set_title("Polynomial fit of a non-linear feature")
```
