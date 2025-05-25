# Plotar as Pontuações BIC

Criamos um `pandas.DataFrame` a partir dos resultados da validação cruzada realizada pela pesquisa em grade. Inverte-se o sinal da pontuação BIC para mostrar o efeito da sua minimização. Usamos `seaborn` para plotar as pontuações BIC.

```python
import pandas as pd
import seaborn as sns

df = pd.DataFrame(grid_search.cv_results_)[
    ["param_n_components", "param_covariance_type", "mean_test_score"]
]
df["mean_test_score"] = -df["mean_test_score"]
df = df.rename(
    columns={
        "param_n_components": "Número de componentes",
        "param_covariance_type": "Tipo de covariância",
        "mean_test_score": "Pontuação BIC",
    }
)
df.sort_values(by="Pontuação BIC").head()

sns.catplot(
    data=df,
    kind="bar",
    x="Número de componentes",
    y="Pontuação BIC",
    hue="Tipo de covariância",
)
plt.show()
```
