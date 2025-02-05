# 绘制特征重要性

我们绘制基于树的特征重要性和排列重要性。排列重要性图显示，对某个特征进行排列最多会使准确率下降 `0.012`，这表明没有一个特征是重要的。这与上面计算出的高测试准确率相矛盾：肯定有一些特征是重要的。排列重要性是在训练集上计算的，以显示模型在训练期间对每个特征的依赖程度。

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
