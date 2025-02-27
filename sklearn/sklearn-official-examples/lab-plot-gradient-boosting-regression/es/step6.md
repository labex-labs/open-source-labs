# Graficar la importancia de permutación

Usaremos el método de permutación para identificar las características con mayor capacidad predictiva.

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
plt.title("Importancia de permutación (conjunto de prueba)")
fig.tight_layout()
plt.show()
```
