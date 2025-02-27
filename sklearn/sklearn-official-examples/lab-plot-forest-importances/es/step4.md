# Importancia de las características basada en la disminución media de la impureza

Las importancias de las características se proporcionan por el atributo ajustado `feature_importances_` y se calculan como la media y la desviación estándar de la acumulación de la disminución de la impureza dentro de cada árbol. Graficaremos la importancia basada en la impureza.

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
