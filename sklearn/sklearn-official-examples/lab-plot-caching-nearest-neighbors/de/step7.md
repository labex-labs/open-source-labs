# Ergebnisse visualisieren

In diesem Schritt werden wir die Ergebnisse der Grid-Suche visualisieren.

```python
# Zeichnen Sie die Ergebnisse der Grid-Suche.
fig, axes = plt.subplots(1, 2, figsize=(8, 4))
axes[0].errorbar(
    x=n_neighbors_list,
    y=grid_model.cv_results_["mean_test_score"],
    yerr=grid_model.cv_results_["std_test_score"],
)
axes[0].set(xlabel="n_neighbors", title="Klassifikationsgenauigkeit")
axes[1].errorbar(
    x=n_neighbors_list,
    y=grid_model.cv_results_["mean_fit_time"],
    yerr=grid_model.cv_results_["std_fit_time"],
    color="r",
)
axes[1].set(xlabel="n_neighbors", title="Anpassungszeit (mit Caching)")
fig.tight_layout()
plt.show()
```
