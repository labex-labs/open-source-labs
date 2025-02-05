# 绘制两个模型的实际值与预测值以及残差与预测值的对比图

我们绘制两个模型的实际值与预测值以及残差与预测值的对比图，并在每个轴的图例中添加得分。

```python
f, (ax0, ax1) = plt.subplots(2, 2, sharey="row", figsize=(6.5, 8))

PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge,
    kind="actual_vs_predicted",
    ax=ax0[0],
    scatter_kwargs={"alpha": 0.5},
)
PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge_with_trans_target,
    kind="actual_vs_predicted",
    ax=ax0[1],
    scatter_kwargs={"alpha": 0.5},
)

for ax, y_pred in zip([ax0[0], ax0[1]], [y_pred_ridge, y_pred_ridge_with_trans_target]):
    for name, score in score.items():
        ax.plot([], [], " ", label=f"{name}={score}")
    ax.legend(loc="upper left")

ax0[0].set_title("岭回归 \n 无目标变换")
ax0[1].set_title("岭回归 \n 有目标变换")

PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge,
    kind="residual_vs_predicted",
    ax=ax1[0],
    scatter_kwargs={"alpha": 0.5},
)
PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge_with_trans_target,
    kind="residual_vs_predicted",
    ax=ax1[1],
    scatter_kwargs={"alpha": 0.5},
)
ax1[0].set_title("岭回归 \n 无目标变换")
ax1[1].set_title("岭回归 \n 有目标变换")

f.suptitle("艾姆斯房屋数据：售价", y=1.05)
plt.tight_layout()
plt.show()
```
