# 결과 시각화

PCA 성분 수에 따른 정확도를 그래프로 시각화합니다.

```python
n_components = grid.cv_results_["param_reduce_dim__n_components"]
test_scores = grid.cv_results_["mean_test_score"]

plt.figure()
plt.bar(n_components, test_scores, width=1.3, color="b")

lower = lower_bound(grid.cv_results_)
plt.axhline(np.max(test_scores), linestyle="--", color="y", label="최고 점수")
plt.axhline(lower, linestyle="--", color=".5", label="최고 점수 - 1 표준편차")

plt.title("모델 복잡도와 교차 검증 점수의 균형")
plt.xlabel("사용된 PCA 성분 수")
plt.ylabel("숫자 분류 정확도")
plt.xticks(n_components.tolist())
plt.ylim((0, 1.0))
plt.legend(loc="upper left")

best_index_ = grid.best_index_

print("최적의 인덱스는 %d입니다" % best_index_)
print("선택된 PCA 성분 수는 %d입니다" % n_components[best_index_])
print(
    "해당 정확도 점수는 %.2f 입니다"
    % grid.cv_results_["mean_test_score"][best_index_]
)
plt.show()
```
