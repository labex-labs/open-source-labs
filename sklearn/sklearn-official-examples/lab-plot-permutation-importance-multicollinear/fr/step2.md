# Tracer l'importance des fonctionnalités

Nous traçons l'importance des fonctionnalités basée sur l'arbre et l'importance de permutation. Le graphique d'importance de permutation montre que permuter une fonctionnalité diminue la précision d'au plus `0,012`, ce qui laisserait croire que aucune des fonctionnalités n'est importante. Cela contredit la haute précision sur le test calculée ci-dessus : certaines fonctionnalités doivent être importantes. L'importance de permutation est calculée sur l'ensemble d'entraînement pour montrer jusqu'à quel point le modèle dépend de chaque fonctionnalité pendant l'entraînement.

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
