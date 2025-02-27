# Analizando los resultados

El atributo `cv_results_` del objeto de búsqueda contiene los resultados de la búsqueda. Conviértelo a un dataframe de pandas utilizando el siguiente código:

```python
results = pd.DataFrame(rsh.cv_results_)
```

La columna `params_str` se crea convirtiendo la columna `params` a una cadena. Elimina las filas duplicadas que tienen los mismos valores de `params_str` e `iter`:

```python
results["params_str"] = results.params.apply(str)
results.drop_duplicates(subset=("params_str", "iter"), inplace=True)
```

Luego, las puntuaciones de prueba promedio se pivotean con respecto al número de iteración y la combinación de parámetros utilizando el método `pivot`:

```python
mean_scores = results.pivot(
    index="iter", columns="params_str", values="mean_test_score"
)
```

Finalmente, grafica las puntuaciones de prueba promedio a lo largo de las iteraciones utilizando el siguiente código:

```python
ax = mean_scores.plot(legend=False, alpha=0.6)

labels = [
    f"iter={i}\nn_samples={rsh.n_resources_[i]}\nn_candidates={rsh.n_candidates_[i]}"
    for i in range(rsh.n_iterations_)
]

ax.set_xticks(range(rsh.n_iterations_))
ax.set_xticklabels(labels, rotation=45, multialignment="left")
ax.set_title("Scores of candidates over iterations")
ax.set_ylabel("mean test score", fontsize=15)
ax.set_xlabel("iterations", fontsize=15)
plt.tight_layout()
plt.show()
```
