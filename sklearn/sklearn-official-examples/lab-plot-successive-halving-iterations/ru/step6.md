# Анализ результатов

Атрибут `cv_results_` объекта поиска содержит результаты поиска. Преобразуйте его в датафрейм `pandas` с использованием следующего кода:

```python
results = pd.DataFrame(rsh.cv_results_)
```

Столбец `params_str` создается путем преобразования столбца `params` в строку. Удалите дублирующие строки, у которых одинаковые значения `params_str` и `iter`:

```python
results["params_str"] = results.params.apply(str)
results.drop_duplicates(subset=("params_str", "iter"), inplace=True)
```

Затем средние тестовые оценки поворачиваются относительно номера итерации и комбинации параметров с использованием метода `pivot`:

```python
mean_scores = results.pivot(
    index="iter", columns="params_str", values="mean_test_score"
)
```

Наконец, постройте график средних тестовых оценок по итерациям с использованием следующего кода:

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
