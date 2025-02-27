# Feature-Wichtigkeit plotten

Wir plotten die baumbasierte Feature-Wichtigkeit und die Permutations-Wichtigkeit. Das Permutations-Wichtigkeit-Diagramm zeigt, dass das Permutieren eines Features die Genauigkeit um maximal `0,012` verringert, was darauf hindeuten würde, dass keine der Features wichtig ist. Dies steht im Widerspruch zur hohen Testgenauigkeit, die oben berechnet wurde: Es muss mindestens ein Feature wichtig sein. Die Permutations-Wichtigkeit wird auf dem Trainingsset berechnet, um zu zeigen, wie stark das Modell bei der Training auf jedes Feature angewiesen ist.

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
