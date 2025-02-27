# 特徴量の重要度をプロットする

ツリーベースの特徴量の重要度と順列重要度をプロットします。順列重要度のプロットでは、特徴量を入れ替えると精度が最大 `0.012` 低下することが示されており、これは特徴量がすべて重要でないことを示唆しています。これは、上で計算した高いテスト精度と矛盾しています。つまり、何らかの特徴量が重要であるはずです。順列重要度は、学習中にモデルが各特徴量にどれだけ依存しているかを示すために学習用セットで計算されます。

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
