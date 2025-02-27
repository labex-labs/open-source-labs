# Visualizar resultados

Visualizaremos los resultados trazando la precisión en función del número de componentes PCA.

```python
n_components = grid.cv_results_["param_reduce_dim__n_components"]
test_scores = grid.cv_results_["mean_test_score"]

plt.figure()
plt.bar(n_components, test_scores, width=1.3, color="b")

lower = lower_bound(grid.cv_results_)
plt.axhline(np.max(test_scores), linestyle="--", color="y", label="Mejor puntuación")
plt.axhline(lower, linestyle="--", color=".5", label="Mejor puntuación - 1 desv. estándar")

plt.title("Equilibrar la complejidad del modelo y la puntuación validada cruzada")
plt.xlabel("Número de componentes PCA utilizados")
plt.ylabel("Precisión de clasificación de dígitos")
plt.xticks(n_components.tolist())
plt.ylim((0, 1.0))
plt.legend(loc="upper left")

best_index_ = grid.best_index_

print("El best_index_ es %d" % best_index_)
print("El número de componentes PCA seleccionados es %d" % n_components[best_index_])
print(
    "La puntuación de precisión correspondiente es %.2f"
    % grid.cv_results_["mean_test_score"][best_index_]
)
plt.show()
```
