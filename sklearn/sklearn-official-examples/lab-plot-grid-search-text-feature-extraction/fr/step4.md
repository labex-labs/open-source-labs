# Visualisation des résultats

Nous pouvons visualiser les résultats de l'ajustement d'hyperparamètres à l'aide de plotly.express. Nous utilisons un graphique en points pour visualiser le compromis entre le temps de calcul de la notation et la moyenne du score de test. Nous pouvons également utiliser des coordonnées parallèles pour visualiser en outre la moyenne du score de test en fonction des hyperparamètres ajustés.

```python
import pandas as pd
import plotly.express as px
import math

def shorten_param(param_name):
    """Supprime les préfixes des composants dans param_name."""
    if "__" est dans param_name:
        return param_name.rsplit("__", 1)[1]
    return param_name

cv_results = pd.DataFrame(random_search.cv_results_)
cv_results = cv_results.rename(shorten_param, axis=1)

param_names = [shorten_param(name) for name in parameter_grid.keys()]
labels = {
    "mean_score_time": "Temps de notation CV (s)",
    "mean_test_score": "Score CV (précision)",
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
        "text": "Compromis entre le temps de notation et la moyenne du score de test",
        "y": 0.95,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

column_results = param_names + ["mean_test_score", "mean_score_time"]

transform_funcs = dict.fromkeys(column_results, lambda x: x)
# Utilisation d'une échelle logarithmique pour alpha
transform_funcs["alpha"] = math.log10
# Les normes L1 sont mappées à l'index 1 et les normes L2 à l'index 2
transform_funcs["norm"] = lambda x: 2 if x == "l2" else 1
# Les unigrammes sont mappés à l'index 1 et les bigrammes à l'index 2
transform_funcs["ngram_range"] = lambda x: x[1]

fig = px.parallel_coordinates(
    cv_results[column_results].apply(transform_funcs),
    color="mean_test_score",
    color_continuous_scale=px.colors.sequential.Viridis_r,
    labels=labels,
)
fig.update_layout(
    title={
        "text": "Représentation en coordonnées parallèles du pipeline de classification de texte",
        "y": 0.99,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

```
