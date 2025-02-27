# Ergebnissevisualisierung

Wir können die Ergebnisse der Hyperparameteroptimierung mit plotly.express visualisieren. Wir verwenden einen Scatterplot, um das Kompromissverhältnis zwischen der Bewertungszeit und der durchschnittlichen Testbewertung zu visualisieren. Wir können auch parallele Koordinaten verwenden, um die durchschnittliche Testbewertung als Funktion der optimierten Hyperparameter weiter zu visualisieren.

```python
import pandas as pd
import plotly.express as px
import math

def shorten_param(param_name):
    """Entfernt die Präfixe der Komponenten in param_name."""
    if "__" in param_name:
        return param_name.rsplit("__", 1)[1]
    return param_name

cv_results = pd.DataFrame(random_search.cv_results_)
cv_results = cv_results.rename(shorten_param, axis=1)

param_names = [shorten_param(name) for name in parameter_grid.keys()]
labels = {
    "mean_score_time": "CV-Score-Zeit (s)",
    "mean_test_score": "CV-Score (Genauigkeit)",
}
fig = px.scatter(
    cv_results,
    x="mean_score_time",
    y="mean_test_score",
    error_x="std_score_time",
    error_y="std_test_score",
    hover_data=param_names,
    labels=labels,
)

fig.update_layout(
    title={
        "text": "Kompromiss zwischen Bewertungszeit und durchschnittlichem Testscore",
        "y": 0.95,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

column_results = param_names + ["mean_test_score", "mean_score_time"]

transform_funcs = dict.fromkeys(column_results, lambda x: x)
# Verwenden einer logarithmischen Skala für alpha
transform_funcs["alpha"] = math.log10
# L1-Normen werden auf Index 1 abgebildet und L2-Normen auf Index 2
transform_funcs["norm"] = lambda x: 2 if x == "l2" else 1
# Unigrams werden auf Index 1 und Bigrams auf Index 2 abgebildet
transform_funcs["ngram_range"] = lambda x: x[1]

fig = px.parallel_coordinates(
    cv_results[column_results].apply(transform_funcs),
    color="mean_test_score",
    color_continuous_scale=px.colors.sequential.Viridis_r,
    labels=labels,
)
fig.update_layout(
    title={
        "text": "Parallele Koordinatenplot des Textklassifizierer-Pipelines",
        "y": 0.99,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

```