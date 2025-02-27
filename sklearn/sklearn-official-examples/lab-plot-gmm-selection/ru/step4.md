# Построение графиков показателей BIC

Мы создаём `pandas.DataFrame` на основе результатов кросс-валидации, выполненной сетевым поиском. Мы переворачиваем знак показателя BIC, чтобы показать эффект минимизации его. Мы используем `seaborn` для построения графиков показателей BIC.

```python
import pandas as pd
import seaborn as sns

df = pd.DataFrame(grid_search.cv_results_)[
    ["param_n_components", "param_covariance_type", "mean_test_score"]
]
df["mean_test_score"] = -df["mean_test_score"]
df = df.rename(
    columns={
        "param_n_components": "Number of components",
        "param_covariance_type": "Type of covariance",
        "mean_test_score": "BIC score",
    }
)
df.sort_values(by="BIC score").head()

sns.catplot(
    data=df,
    kind="bar",
    x="Number of components",
    y="BIC score",
    hue="Type of covariance",
)
plt.show()
```
