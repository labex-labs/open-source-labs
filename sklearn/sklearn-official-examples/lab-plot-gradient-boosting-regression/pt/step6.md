# Plotar a Importância por Permutação

Usaremos o método de permutação para identificar as características mais preditivas.

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
plt.title("Importância por Permutação (conjunto de teste)")
fig.tight_layout()
plt.show()
```
