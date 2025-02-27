# Visualiser les résultats

Nous allons visualiser les résultats en traçant la précision en fonction du nombre de composants PCA.

```python
n_components = grid.cv_results_["param_reduce_dim__n_components"]
test_scores = grid.cv_results_["mean_test_score"]

plt.figure()
plt.bar(n_components, test_scores, width=1.3, color="b")

lower = lower_bound(grid.cv_results_)
plt.axhline(np.max(test_scores), linestyle="--", color="y", label="Meilleur score")
plt.axhline(lower, linestyle="--", color=".5", label="Meilleur score - 1 écart-type")

plt.title("Équilibrer la complexité du modèle et le score de validation croisée")
plt.xlabel("Nombre de composants PCA utilisés")
plt.ylabel("Précision de classification des chiffres")
plt.xticks(n_components.tolist())
plt.ylim((0, 1.0))
plt.legend(loc="upper left")

best_index_ = grid.best_index_

print("Le best_index_ est %d" % best_index_)
print("Le nombre de composants PCA sélectionnés est %d" % n_components[best_index_])
print(
    "Le score de précision correspondant est %.2f"
    % grid.cv_results_["mean_test_score"][best_index_]
)
plt.show()
```
