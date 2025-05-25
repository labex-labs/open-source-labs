# Comparar Resultados

Vamos comparar os resultados de diferentes estratégias de imputação usando um gráfico de barras.

```python
scores = pd.concat(
    [score_full_data, score_simple_imputer, score_iterative_imputer],
    keys=["Original", "SimpleImputer", "IterativeImputer"],
    axis=1,
)

fig, ax = plt.subplots(figsize=(13, 6))
means = -scores.mean()
errors = scores.std()
means.plot.barh(xerr=errors, ax=ax)
ax.set_title("Regressão de Habitação da Califórnia com Diferentes Métodos de Imputação")
ax.set_xlabel("MSE (menor é melhor)")
ax.set_yticks(np.arange(means.shape[0]))
ax.set_yticklabels([" w/ ".join(label) for label in means.index.tolist()])
plt.tight_layout(pad=1)
plt.show()
```
