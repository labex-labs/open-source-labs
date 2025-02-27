# Tracer les scores BIC

Nous créons un `pandas.DataFrame` à partir des résultats de la validation croisée effectuée par la recherche en grille. Nous inversons à nouveau le signe du score BIC pour montrer l'effet de sa minimisation. Nous utilisons `seaborn` pour tracer les scores BIC.

```python
import pandas as pd
import seaborn as sns

df = pd.DataFrame(grid_search.cv_results_)[
    ["param_n_components", "param_covariance_type", "mean_test_score"]
]
df["mean_test_score"] = -df["mean_test_score"]
df = df.rename(
    columns={
        "param_n_components": "Nombre de composants",
        "param_covariance_type": "Type de covariance",
        "mean_test_score": "Score BIC",
    }
)
df.sort_values(by="Score BIC").head()

sns.catplot(
    data=df,
    kind="bar",
    x="Nombre de composants",
    y="Score BIC",
    hue="Type de covariance",
)
plt.show()
```
