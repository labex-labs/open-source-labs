# 점수의 표준 오차를 사용하여 다항 회귀 플롯 그리기

오차 막대는 쿼리 지점의 예측된 가우시안 분포의 한 표준 편차를 나타냅니다. ARD 회귀가 두 모델 모두 기본 매개변수를 사용할 때 실제 값을 가장 잘 포착하는 데 주목하십시오. 그러나 베이지안 릿지의 `lambda_init` 하이퍼매개변수를 더 줄이면 편향을 줄일 수 있습니다. 마지막으로, 다항 회귀의 본질적인 한계로 인해 두 모델 모두 외삽 시 실패합니다.

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
