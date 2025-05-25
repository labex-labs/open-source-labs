# 변수 중요도 (Permutation) 시각화

변수의 예측력을 평가하기 위해 순열 방법을 사용합니다.

```python
result = permutation_importance(
    reg, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)
sorted_idx = result.importances_mean.argsort()
plt.subplot(1, 2, 2)
plt.boxplot(
    result.importances[sorted_idx].T,
    vert=False,
    labels=np.array(diabetes.feature_names)[sorted_idx],
)
plt.title("순열 중요도 (테스트 세트)")
fig.tight_layout()
plt.show()
```
