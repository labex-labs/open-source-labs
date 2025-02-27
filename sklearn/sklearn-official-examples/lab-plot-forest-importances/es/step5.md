# Importancia de las características basada en la permutación de características

La importancia de las características basada en la permutación supera las limitaciones de la importancia de las características basada en la impureza: no tienen un sesgo hacia las características de alta cardinalidad y se pueden calcular en un conjunto de prueba omitido. Calcularemos la importancia de la permutación completa. Las características se barajan n veces y el modelo se ajusta nuevamente para estimar su importancia. Graficaremos la clasificación de importancia.

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
