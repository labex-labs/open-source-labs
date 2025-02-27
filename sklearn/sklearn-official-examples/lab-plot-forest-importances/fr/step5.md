# Importance des caractéristiques basée sur la permutation des caractéristiques

L'importance des caractéristiques basée sur la permutation surmonte les limites de l'importance des caractéristiques basée sur l'impureté : elles n'ont pas de biais en faveur des caractéristiques à forte cardinalité et peuvent être calculées sur un ensemble de test laissé de côté. Nous allons calculer l'importance de permutation complète. Les caractéristiques sont mélangées n fois et le modèle est réajusté pour estimer son importance. Nous allons tracer le classement d'importance.

```python
start_time = time.time()
result = permutation_importance(
    forest, X_test, y_test, n_repeats=10, random_state=42, n_jobs=2
)
elapsed_time = time.time() - start_time
print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

forest_importances = pd.Series(result.importances_mean, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=result.importances_std, ax=ax)
ax.set_title("Feature importances using permutation on full model")
ax.set_ylabel("Mean accuracy decrease")
fig.tight_layout()
plt.show()
```
