# Visualizar los resultados

En este paso, visualizaremos los resultados de la búsqueda de cuadrícula.

```python
# Grafique los resultados de la búsqueda de cuadrícula.
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].errorbar(
    x=n_neighbors_list,
    y=grid_model.cv_results_["mean_test_score"],
    yerr=grid_model.cv_results_["std_test_score"],
)
axes[0].set(xlabel="n_neighbors", title="Precisión de clasificación")
axes[1].errorbar(
    x=n_neighbors_list,
    y=grid_model.cv_results_["mean_fit_time"],
    yerr=grid_model.cv_results_["std_fit_time"],
    color="r",
)
axes[1].set(xlabel="n_neighbors", title="Tiempo de ajuste (con almacenamiento en caché)")
fig.tight_layout()
plt.show()
```
