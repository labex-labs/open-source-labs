# Analyzing the Results

The `cv_results_` attribute of the search object contains the results of the search. Convert it to a pandas dataframe using the following code:

```python
results = pd.DataFrame(rsh.cv_results_)
```

The `params_str` column is created by converting the `params` column to a string. Remove duplicate rows that have the same `params_str` and `iter` values:

```python
results["params_str"] = results.params.apply(str)
results.drop_duplicates(subset=("params_str", "iter"), inplace=True)
```

The mean test scores are then pivoted with respect to the iteration number and parameter combination using the `pivot` method:

```python
mean_scores = results.pivot(
    index="iter", columns="params_str", values="mean_test_score"
)
```

Finally, plot the mean test scores over the iterations using the following code:

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


