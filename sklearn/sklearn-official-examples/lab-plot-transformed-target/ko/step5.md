# 두 모델의 실제 값 대 예측 값 플롯

두 모델의 실제 값 대 예측 값을 플롯하고 각 축의 범례에 점수를 추가합니다.

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

ax0.set_title("타겟 변환 없이 Ridge 회귀")
ax1.set_title("타겟 변환을 사용한 Ridge 회귀")
f.suptitle("합성 데이터", y=1.05)
plt.tight_layout()
```
