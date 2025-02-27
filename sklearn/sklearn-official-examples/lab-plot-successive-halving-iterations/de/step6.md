# Analysieren der Ergebnisse

Das Attribut `cv_results_` des Suchobjekts enthält die Ergebnisse der Suche. Konvertiere es in einen pandas-DataFrame mit dem folgenden Code:

```python
results = pd.DataFrame(rsh.cv_results_)
```

Die Spalte `params_str` wird erstellt, indem die Spalte `params` in einen String umgewandelt wird. Entferne doppelte Zeilen, die die gleichen `params_str`- und `iter`-Werte haben:

```python
results["params_str"] = results.params.apply(str)
results.drop_duplicates(subset=("params_str", "iter"), inplace=True)
```

Die durchschnittlichen Testscores werden dann mithilfe der `pivot`-Methode in Bezug auf die Iterationsnummer und die Parameterkombination umgeformt:

```python
mean_scores = results.pivot(
    index="iter", columns="params_str", values="mean_test_score"
)
```

Schließlich werden die durchschnittlichen Testscores über die Iterationen mit dem folgenden Code geplottet:

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
