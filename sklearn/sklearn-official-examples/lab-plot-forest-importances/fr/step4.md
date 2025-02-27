# Importance des caractéristiques basée sur la diminution moyenne de l'impureté

Les importances des caractéristiques sont fournies par l'attribut ajusté `feature_importances_` et elles sont calculées comme la moyenne et l'écart-type de l'accumulation de la diminution d'impureté au sein de chaque arbre. Nous allons tracer l'importance basée sur l'impureté.

```python
start_time = time.time()
importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_], axis=0)
elapsed_time = time.time() - start_time

print(f"Elapsed time to compute the importances: {elapsed_time:.3f} seconds")

forest_importances = pd.Series(importances, index=feature_names)

fig, ax = plt.subplots()
forest_importances.plot.bar(yerr=std, ax=ax)
ax.set_title("Feature importances using MDI")
ax.set_ylabel("Mean decrease in impurity")
fig.tight_layout()
```
