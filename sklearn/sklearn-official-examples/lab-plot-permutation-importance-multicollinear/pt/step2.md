# Plotar a Importância das Características

Plotamos a importância das características baseadas em árvores e a importância por permutação. O gráfico de importância por permutação mostra que a permutação de uma característica reduz a precisão no máximo em `0,012`, o que sugeria que nenhuma das características é importante. Isso contradiz a alta precisão de teste calculada acima: alguma característica deve ser importante. A importância por permutação é calculada no conjunto de treinamento para mostrar em que medida o modelo depende de cada característica durante o treinamento.

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
