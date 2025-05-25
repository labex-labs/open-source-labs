# 결과 시각화

이 단계에서는 그리드 검색 결과를 시각화합니다.

```python
# 그리드 검색 결과를 플롯합니다.
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].errorbar(
    x=n_neighbors_list,
    y=grid_model.cv_results_["mean_test_score"],
    yerr=grid_model.cv_results_["std_test_score"],
)
axes[0].set(xlabel="n_neighbors", title="분류 정확도")
axes[1].errorbar(
    x=n_neighbors_list,
    y=grid_model.cv_results_["mean_fit_time"],
    yerr=grid_model.cv_results_["std_fit_time"],
    color="r",
)
axes[1].set(xlabel="n_neighbors", title="적합 시간 (캐싱 포함)")
fig.tight_layout()
plt.show()
```
