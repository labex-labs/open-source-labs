# Visualização de Resultados

Podemos visualizar os resultados do ajuste de hiperparâmetros usando plotly.express. Usamos um gráfico de dispersão para visualizar o trade-off entre o tempo de pontuação e a média da pontuação de teste. Também podemos usar coordenadas paralelas para visualizar ainda mais a média da pontuação de teste em função dos hiperparâmetros ajustados.

```python
import pandas as pd
import plotly.express as px
import math

def shorten_param(param_name):
    """Remove os prefixos dos componentes em param_name."""
    if "__" in param_name:
        return param_name.rsplit("__", 1)[1]
    return param_name

cv_results = pd.DataFrame(random_search.cv_results_)
cv_results = cv_results.rename(shorten_param, axis=1)

param_names = [shorten_param(name) for name in parameter_grid.keys()]
labels = {
    "mean_score_time": "Tempo de Pontuação CV (s)",
    "mean_test_score": "Pontuação CV (precisão)",
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
        "text": "trade-off entre tempo de pontuação e média da pontuação de teste",
        "y": 0.95,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

column_results = param_names + ["mean_test_score", "mean_score_time"]

transform_funcs = dict.fromkeys(column_results, lambda x: x)
# Usando uma escala logarítmica para alpha
transform_funcs["alpha"] = math.log10
# As normas L1 são mapeadas para o índice 1, e as normas L2 para o índice 2
transform_funcs["norm"] = lambda x: 2 if x == "l2" else 1
# Unigramas são mapeados para o índice 1 e bigramas para o índice 2
transform_funcs["ngram_range"] = lambda x: x[1]

fig = px.parallel_coordinates(
    cv_results[column_results].apply(transform_funcs),
    color="mean_test_score",
    color_continuous_scale=px.colors.sequential.Viridis_r,
    labels=labels,
)
fig.update_layout(
    title={
        "text": "Gráfico de coordenadas paralelas do pipeline do classificador de texto",
        "y": 0.99,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

```
