# Построить график важности признаков

Мы строим важность признаков, основанную на деревьях, и важность перестановок. График важности перестановок показывает, что перестановка признака понижает точность максимум на `0,012`, что может означать, что ни один из признаков не имеет важности. Это противоречит высокой точности теста, вычисленной выше: некоторые признаки должны быть важными. Важность перестановок вычисляется на обучающем наборе, чтобы показать, насколько модель зависит от каждого признака во время обучения.

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
