# Visualizar Resultados

Vamos visualizar os resultados traçando a precisão versus o número de componentes PCA.

```python
n_components = grid.cv_results_["param_reduce_dim__n_components"]
test_scores = grid.cv_results_["mean_test_score"]

plt.figure()
plt.bar(n_components, test_scores, width=1.3, color="b")

lower = lower_bound(grid.cv_results_)
plt.axhline(np.max(test_scores), linestyle="--", color="y", label="Melhor pontuação")
plt.axhline(lower, linestyle="--", color=".5", label="Melhor pontuação - 1 desvio padrão")

plt.title("Equilibrar a complexidade do modelo e a pontuação cruzada")
plt.xlabel("Número de componentes PCA usados")
plt.ylabel("Precisão de classificação de dígitos")
plt.xticks(n_components.tolist())
plt.ylim((0, 1.0))
plt.legend(loc="upper left")

best_index_ = grid.best_index_

print("O melhor índice é %d" % best_index_)
print("O número de componentes selecionado é %d" % n_components[best_index_])
print(
    "A pontuação de precisão correspondente é %.2f"
    % grid.cv_results_["mean_test_score"][best_index_]
)
plt.show()
```
