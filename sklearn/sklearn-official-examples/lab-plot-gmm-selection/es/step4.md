# Grafica las puntuaciones BIC

Creamos un `pandas.DataFrame` a partir de los resultados de la validación cruzada realizada por la búsqueda en cuadrícula. Volvemos a invertir el signo de la puntuación BIC para mostrar el efecto de minimizarla. Utilizamos `seaborn` para graficar las puntuaciones BIC.

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
        "param_covariance_type": "Tipo de covarianza",
        "mean_test_score": "Puntuación BIC",
    }
)
df.sort_values(by="Puntuación BIC").head()

sns.catplot(
    data=df,
    kind="bar",
    x="Número de componentes",
    y="Puntuación BIC",
    hue="Tipo de covarianza",
)
plt.show()
```
