# Comparing Random Forests and Histogram Gradient Boosting Models for Regression

## Introduction

In this lab, we will compare the performance of two popular ensemble models, Random Forest (RF) and Histogram Gradient Boosting (HGBT), for a regression dataset in terms of score and computation time. We will vary the parameters that control the number of trees according to each estimator and plot the results to visualize the trade-off between elapsed computing time and mean test score.

## Steps

### Step 1: Load Dataset

We will load the California housing dataset using the scikit-learn `fetch_california_housing` function. This dataset consists of 20,640 samples and 8 features.

```python
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True, as_frame=True)
n_samples, n_features = X.shape

print(f"The dataset consists of {n_samples} samples and {n_features} features")
```

### Step 2: Define Models and Parameter Grids

We will define two models, Random Forest and Histogram Gradient Boosting, with their corresponding parameter grids using scikit-learn's `RandomForestRegressor`, `HistGradientBoostingRegressor`, and `GridSearchCV` classes. We will also set the number of physical cores on the host machine to use for parallel processing.

```python
import joblib
import pandas as pd
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.model_selection import GridSearchCV, KFold

N_CORES = joblib.cpu_count(only_physical_cores=True)

models = {
    "Random Forest": RandomForestRegressor(
        min_samples_leaf=5, random_state=0, n_jobs=N_CORES
    ),
    "Hist Gradient Boosting": HistGradientBoostingRegressor(
        max_leaf_nodes=15, random_state=0, early_stopping=False
    ),
}

param_grids = {
    "Random Forest": {"n_estimators": [10, 20, 50, 100]},
    "Hist Gradient Boosting": {"max_iter": [10, 20, 50, 100, 300, 500]},
}

cv = KFold(n_splits=4, shuffle=True, random_state=0)

results = []

for name, model in models.items():
    grid_search = GridSearchCV(
        estimator=model,
        param_grid=param_grids[name],
        return_train_score=True,
        cv=cv,
    ).fit(X, y)

    result = {"model": name, "cv_results": pd.DataFrame(grid_search.cv_results_)}
    results.append(result)
```

### Step 3: Compute Scores and Computation Times

We will compute the mean fit and score times for each combination of hyperparameters using the `cv_results_` attribute of the `GridSearchCV` object. We will then plot the results using `plotly.express.scatter` and `plotly.express.line` to visualize the trade-off between elapsed computing time and mean test score.

```python
import plotly.express as px
import plotly.colors as colors
from plotly.subplots import make_subplots

fig = make_subplots(
    rows=1,
    cols=2,
    shared_yaxes=True,
    subplot_titles=["Train time vs score", "Predict time vs score"],
)
model_names = [result["model"] for result in results]
colors_list = colors.qualitative.Plotly * (
    len(model_names) // len(colors.qualitative.Plotly) + 1
)

for idx, result in enumerate(results):
    cv_results = result["cv_results"].round(3)
    model_name = result["model"]
    param_name = list(param_grids[model_name].keys())[0]
    cv_results[param_name] = cv_results["param_" + param_name]
    cv_results["model"] = model_name

    scatter_fig = px.scatter(
        cv_results,
        x="mean_fit_time",
        y="mean_test_score",
        error_x="std_fit_time",
        error_y="std_test_score",
        hover_data=param_name,
        color="model",
    )
    line_fig = px.line(
        cv_results,
        x="mean_fit_time",
        y="mean_test_score",
    )

    scatter_trace = scatter_fig["data"][0]
    line_trace = line_fig["data"][0]
    scatter_trace.update(marker=dict(color=colors_list[idx]))
    line_trace.update(line=dict(color=colors_list[idx]))
    fig.add_trace(scatter_trace, row=1, col=1)
    fig.add_trace(line_trace, row=1, col=1)

    scatter_fig = px.scatter(
        cv_results,
        x="mean_score_time",
        y="mean_test_score",
        error_x="std_score_time",
        error_y="std_test_score",
        hover_data=param_name,
    )
    line_fig = px.line(
        cv_results,
        x="mean_score_time",
        y="mean_test_score",
    )

    scatter_trace = scatter_fig["data"][0]
    line_trace = line_fig["data"][0]
    scatter_trace.update(marker=dict(color=colors_list[idx]))
    line_trace.update(line=dict(color=colors_list[idx]))
    fig.add_trace(scatter_trace, row=1, col=2)
    fig.add_trace(line_trace, row=1, col=2)

fig.update_layout(
    xaxis=dict(title="Train time (s) - lower is better"),
    yaxis=dict(title="Test R2 score - higher is better"),
    xaxis2=dict(title="Predict time (s) - lower is better"),
    legend=dict(x=0.72, y=0.05, traceorder="normal", borderwidth=1),
    title=dict(x=0.5, text="Speed-score trade-off of tree-based ensembles"),
)
```

### Step 4: Interpret Results

We can observe that both HGBT and RF models improve when increasing the number of trees in the ensemble. However, the scores reach a plateau where adding new trees just makes fitting and scoring slower. The RF model reaches such plateau earlier and can never reach the test score of the largest HGBDT model. HGBT models uniformly dominate the RF models in the "test score vs training speed trade-off" and the "test score vs prediction speed" trade-off can also be more favorable to HGBT. HGBT almost always offers a more favorable speed-accuracy trade-off than RF, either with the default hyper-parameters or including the hyper-parameter tuning cost.

## Summary

In this lab, we compared the performance of two popular ensemble models, Random Forest and Histogram Gradient Boosting, for a regression dataset in terms of score and computation time. We varied the parameters that control the number of trees according to each estimator and plotted the results to visualize the trade-off between elapsed computing time and mean test score. We observed that HGBT models uniformly dominate the RF models in the "test score vs training speed trade-off" and the "test score vs prediction speed" trade-off can also be more favorable to HGBT. HGBT almost always offers a more favorable speed-accuracy trade-off than RF, either with the default hyper-parameters or including the hyper-parameter tuning cost.
