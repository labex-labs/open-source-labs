# 결과 플롯

각 모델의 테스트 오류, 분류 오류 및 부스팅 가중치를 플롯합니다.

```python
n_trees_discrete = len(bdt_discrete)
n_trees_real = len(bdt_real)

# 부스팅은 조기 종료될 수 있지만, 다음 배열은 항상
# n_estimators 길이입니다. 여기서 실제 트리 수에 맞춰 잘라냅니다.
discrete_estimator_errors = bdt_discrete.estimator_errors_[:n_trees_discrete]
real_estimator_errors = bdt_real.estimator_errors_[:n_trees_real]
discrete_estimator_weights = bdt_discrete.estimator_weights_[:n_trees_discrete]

plt.figure(figsize=(15, 5))

plt.subplot(131)
plt.plot(range(1, n_trees_discrete + 1), discrete_test_errors, c="black", label="SAMME")
plt.plot(
    range(1, n_trees_real + 1),
    real_test_errors,
    c="black",
    linestyle="dashed",
    label="SAMME.R",
)
plt.legend()
plt.ylim(0.18, 0.62)
plt.ylabel("테스트 오류")
plt.xlabel("트리 개수")

plt.subplot(132)
plt.plot(
    range(1, n_trees_discrete + 1),
    discrete_estimator_errors,
    "b",
    label="SAMME",
    alpha=0.5,
)
plt.plot(
    range(1, n_trees_real + 1), real_estimator_errors, "r", label="SAMME.R", alpha=0.5
)
plt.legend()
plt.ylabel("오류")
plt.xlabel("트리 개수")
plt.ylim((0.2, max(real_estimator_errors.max(), discrete_estimator_errors.max()) * 1.2))
plt.xlim((-20, len(bdt_discrete) + 20))

plt.subplot(133)
plt.plot(range(1, n_trees_discrete + 1), discrete_estimator_weights, "b", label="SAMME")
plt.legend()
plt.ylabel("가중치")
plt.xlabel("트리 개수")
plt.ylim((0, discrete_estimator_weights.max() * 1.2))
plt.xlim((-20, n_trees_discrete + 20))

# y 축 레이블이 겹치는 것을 방지
plt.subplots_adjust(wspace=0.25)
plt.show()
```
