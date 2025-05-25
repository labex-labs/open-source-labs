# 최종 결론

두 모델이 외삽할 가능성에 대한 최종적인 언급을 할 수 있습니다. 모델이 사인 패턴을 계속 예측할 것으로 관찰됩니다.

```python
kernel = 1.0 * ExpSineSquared(1.0, 5.0, periodicity_bounds=(1e-2, 1e1)) * RBF(
    length_scale=15, length_scale_bounds="fixed"
) + WhiteKernel(1e-1)
gaussian_process = GaussianProcessRegressor(kernel=kernel)

gaussian_process.fit(training_data, training_noisy_target)

mean_predictions_gpr, std_predictions_gpr = gaussian_process.predict(
    data, return_std=True,
)

plt.plot(data, target, label="True signal", linewidth=2, linestyle="dashed")
plt.scatter(
    training_data,
    training_noisy_target,
    color="black",
    label="Noisy measurements",
)
plt.plot(
    data,
    mean_predictions_gpr,
    label="Gaussian process regressor",
    linewidth=2,
    linestyle="dotted",
)
plt.fill_between(
    data.ravel(),
    mean_predictions_gpr - std_predictions_gpr,
    mean_predictions_gpr + std_predictions_gpr,
    color="tab:green",
    alpha=0.2,
)
plt.legend(loc="lower right")
plt.xlabel("data")
plt.ylabel("target")
_ = plt.title("커널 릿지와 가우시안 프로세스 회귀자 비교")
```
