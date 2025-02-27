# Visualiser les résultats

Dans cette étape, nous allons visualiser les résultats de la recherche en grille.

```python
# Tracez les résultats de la recherche en grille.
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].errorbar(
    x=n_neighbors_list,
    y=grid_model.cv_results_["mean_test_score"],
    yerr=grid_model.cv_results_["std_test_score"],
)
axes[0].set(xlabel="n_neighbors", title="Précision de classification")
axes[1].errorbar(
    x=n_neighbors_list,
    y=grid_model.cv_results_["mean_fit_time"],
    yerr=grid_model.cv_results_["std_fit_time"],
    color="r",
)
axes[1].set(xlabel="n_neighbors", title="Temps d'ajustement (avec mise en cache)")
fig.tight_layout()
plt.show()
```
