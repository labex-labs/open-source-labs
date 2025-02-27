# Graficar la importancia de las características

Graficamos la importancia de las características basada en árboles y la importancia de permutación. La gráfica de importancia de permutación muestra que la permutación de una característica reduce la precisión como máximo en `0.012`, lo que sugeriría que ninguna de las características es importante. Esto está en contradicción con la alta precisión en la prueba calculada anteriormente: algunas características deben ser importantes. La importancia de permutación se calcula en el conjunto de entrenamiento para mostrar en qué medida el modelo depende de cada característica durante el entrenamiento.

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
