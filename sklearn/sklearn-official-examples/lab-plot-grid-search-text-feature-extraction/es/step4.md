# Visualización de resultados

Podemos visualizar los resultados del ajuste de hiperparámetros usando plotly.express. Usamos un diagrama de dispersión para visualizar el equilibrio entre el tiempo de puntuación y la puntuación promedio de prueba. También podemos usar coordenadas paralelas para visualizar aún más la puntuación promedio de prueba en función de los hiperparámetros ajustados.

```python
import pandas as pd
import plotly.express as px
import math

def shorten_param(param_name):
    """Elimina los prefijos de los componentes en param_name."""
    if "__" está en param_name:
        return param_name.rsplit("__", 1)[1]
    return param_name

cv_results = pd.DataFrame(random_search.cv_results_)
cv_results = cv_results.rename(shorten_param, axis=1)

param_names = [shorten_param(name) for name in parameter_grid.keys()]
labels = {
    "mean_score_time": "Tiempo de puntuación CV (s)",
    "mean_test_score": "Puntuación CV (precision)",
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
        "text": "equilibrio entre el tiempo de puntuación y la puntuación promedio de prueba",
        "y": 0.95,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

column_results = param_names + ["mean_test_score", "mean_score_time"]

transform_funcs = dict.fromkeys(column_results, lambda x: x)
# Usando una escala logarítmica para alpha
transform_funcs["alpha"] = math.log10
# Las normas L1 se asignan al índice 1 y las normas L2 al índice 2
transform_funcs["norm"] = lambda x: 2 si x == "l2" else 1
# Los unigramas se asignan al índice 1 y los bigramas al índice 2
transform_funcs["ngram_range"] = lambda x: x[1]

fig = px.parallel_coordinates(
    cv_results[column_results].apply(transform_funcs),
    color="mean_test_score",
    color_continuous_scale=px.colors.sequential.Viridis_r,
    labels=labels,
)
fig.update_layout(
    title={
        "text": "Diagrama de coordenadas paralelas de la canalización de clasificador de texto",
        "y": 0.99,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

```
