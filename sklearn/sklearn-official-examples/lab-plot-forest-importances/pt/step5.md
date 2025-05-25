# Importância das Características baseada na Permutação de Características

A importância das características por permutação supera as limitações da importância das características baseada na impureza: não apresentam viés para características de alta cardinalidade e podem ser calculadas em um conjunto de teste deixado de fora. Calcularemos a importância por permutação completa. As características são embaralhadas n vezes e o modelo é reajustado para estimar a sua importância. Vamos plotar a classificação de importância.

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
ax.set_title("Importâncias das características usando permutação no modelo completo")
ax.set_ylabel("Diminuição média de precisão")
fig.tight_layout()
plt.show()
```
