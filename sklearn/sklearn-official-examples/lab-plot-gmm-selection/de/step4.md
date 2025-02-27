# Zeichnen Sie die BIC-Werte

Wir erstellen ein `pandas.DataFrame` aus den Ergebnissen der Kreuzvalidierung, die durch die Grid-Suche durchgeführt wurde. Wir kehren das Vorzeichen des BIC-Werts um, um die Wirkung der Minimierung zu zeigen. Wir verwenden `seaborn`, um die BIC-Werte zu zeichnen.

```python
import pandas as pd
import seaborn as sns

df = pd.DataFrame(grid_search.cv_results_)[
    ["param_n_components", "param_covariance_type", "mean_test_score"]
]
df["mean_test_score"] = -df["mean_test_score"]
df = df.rename(
    columns={
        "param_n_components": "Anzahl der Komponenten",
        "param_covariance_type": "Typ der Kovarianz",
        "mean_test_score": "BIC-Wert",
    }
)
df.sort_values(by="BIC-Wert").head()

sns.catplot(
    data=df,
    kind="bar",
    x="Anzahl der Komponenten",
    y="BIC-Wert",
    hue="Typ der Kovarianz",
)
plt.show()
```
