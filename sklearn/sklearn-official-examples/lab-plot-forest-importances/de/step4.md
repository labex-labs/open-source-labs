# Merkmalswichtigkeit basierend auf der durchschnittlichen Verringerung der Unreinheit

Die Merkmalswichtigkeiten werden durch das angepasste Attribut `feature_importances_` bereitgestellt und berechnet sich als Mittelwert und Standardabweichung der Akkumulation der Unreinheitsverringerung innerhalb jedes Baumes. Wir werden die auf Unreinheit basierende Wichtigkeit plotten.

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
