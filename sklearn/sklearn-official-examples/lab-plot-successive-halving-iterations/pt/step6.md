# Analisando os Resultados

O atributo `cv_results_` do objeto de pesquisa contém os resultados da pesquisa. Converta-o em um DataFrame pandas usando o código a seguir:

```python
results = pd.DataFrame(rsh.cv_results_)
```

A coluna `params_str` é criada convertendo a coluna `params` para uma string. Remova as linhas duplicadas que possuem os mesmos valores para `params_str` e `iter`:

```python
results["params_str"] = results.params.apply(str)
results.drop_duplicates(subset=("params_str", "iter"), inplace=True)
```

As pontuações médias de teste são então pivotadas em relação ao número da iteração e à combinação de parâmetros usando o método `pivot`:

```python
mean_scores = results.pivot(
    index="iter", columns="params_str", values="mean_test_score"
)
```

Finalmente, plote as pontuações médias de teste ao longo das iterações usando o código a seguir:

```python
ax = mean_scores.plot(legend=False, alpha=0.6)

labels = [
    f"iter={i}\nn_samples={rsh.n_resources_[i]}\nn_candidates={rsh.n_candidates_[i]}"
    for i in range(rsh.n_iterations_)
]

ax.set_xticks(range(rsh.n_iterations_))
ax.set_xticklabels(labels, rotation=45, multialignment="left")
ax.set_title("Pontuações dos candidatos ao longo das iterações")
ax.set_ylabel("pontuação média de teste", fontsize=15)
ax.set_xlabel("iterações", fontsize=15)
plt.tight_layout()
plt.show()
```
