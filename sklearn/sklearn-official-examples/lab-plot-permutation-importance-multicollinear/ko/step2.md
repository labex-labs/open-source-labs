# 특징 중요도 시각화

트리 기반 특징 중요도와 순열 중요도를 시각화합니다. 순열 중요도 플롯은 특징을 섞으면 정확도가 최대 0.012 만큼 감소한다는 것을 보여주는데, 이는 특징 중 중요한 것이 없다는 것을 시사합니다. 이는 위에서 계산된 높은 테스트 정확도와 모순됩니다. 몇몇 특징은 중요해야 합니다. 순열 중요도는 학습 과정에서 모델이 각 특징에 얼마나 의존하는지 보여주기 위해 학습 데이터셋에서 계산됩니다.

```python
result = permutation_importance(clf, X_train, y_train, n_repeats=10, random_state=42)
perm_sorted_idx = result.importances_mean.argsort()

tree_importance_sorted_idx = np.argsort(clf.feature_importances_)
tree_indices = np.arange(0, len(clf.feature_importances_)) + 0.5

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 8))
ax1.barh(tree_indices, clf.feature_importances_[tree_importance_sorted_idx], height=0.7)
ax1.set_yticks(tree_indices)
ax1.set_yticklabels(data.feature_names[tree_importance_sorted_idx])
ax1.set_ylim((0, len(clf.feature_importances_)))
ax2.boxplot(
    result.importances[perm_sorted_idx].T,
    vert=False,
    labels=data.feature_names[perm_sorted_idx],
)
fig.tight_layout()
plt.show()
```
