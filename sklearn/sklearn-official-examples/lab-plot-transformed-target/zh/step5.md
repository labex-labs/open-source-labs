# 绘制两个模型的实际值与预测值对比图

我们绘制两个模型的实际值与预测值对比图，并在每个轴的图例中添加得分。

```python
f, (ax0, ax1) = plt.subplots(1, 2, sharey=True)

PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge,
    kind="actual_vs_predicted",
    ax=ax0,
    scatter_kwargs={"alpha": 0.5},
)
PredictionErrorDisplay.from_predictions(
    y_test,
    y_pred_ridge_with_trans_target,
    kind="actual_vs_predicted",
    ax=ax1,
    scatter_kwargs={"alpha": 0.5},
)

for ax, y_pred in zip([ax0, ax1], [y_pred_ridge, y_pred_ridge_with_trans_target]):
    for name, score in score.items():
        ax.plot([], [], " ", label=f"{name}={score}")
    ax.legend(loc="upper left")

ax0.set_title("岭回归 \n 无目标转换")
ax1.set_title("岭回归 \n 有目标转换")
f.suptitle("合成数据", y=1.05)
plt.tight_layout()
```
