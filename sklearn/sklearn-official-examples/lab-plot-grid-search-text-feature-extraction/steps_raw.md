# Text Feature Extraction and Evaluation

## Introduction

The scikit-learn library provides tools for text feature extraction and evaluation. In this lab, we will use the 20newsgroups dataset to demonstrate how to extract features from text data, build a pipeline, and evaluate the performance of the model using hyperparameter tuning.

## Steps

### Step 1: Load Data

We will load the 20newsgroups dataset which is a collection of approximately 20,000 newsgroup documents across 20 different categories. For this lab, we will focus on two categories: alt.atheism and talk.religion.misc.

```python
from sklearn.datasets import fetch_20newsgroups

categories = [
    "alt.atheism",
    "talk.religion.misc",
]

data_train = fetch_20newsgroups(
    subset="train",
    categories=categories,
    shuffle=True,
    random_state=42,
    remove=("headers", "footers", "quotes"),
)

data_test = fetch_20newsgroups(
    subset="test",
    categories=categories,
    shuffle=True,
    random_state=42,
    remove=("headers", "footers", "quotes"),
)

print(f"Loading 20 newsgroups dataset for {len(data_train.target_names)} categories:")
print(data_train.target_names)
print(f"{len(data_train.data)} documents")
```

### Step 2: Define Pipeline with Hyperparameter Tuning

We define a pipeline that combines a text feature vectorizer with a simple classifier for text classification. We will use Complement Naive Bayes as the classifier and TfidfVectorizer for feature extraction.

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import ComplementNB
from sklearn.pipeline import Pipeline
import numpy as np

pipeline = Pipeline(
    [
        ("vect", TfidfVectorizer()),
        ("clf", ComplementNB()),
    ]
)

parameter_grid = {
    "vect__max_df": (0.2, 0.4, 0.6, 0.8, 1.0),
    "vect__min_df": (1, 3, 5, 10),
    "vect__ngram_range": ((1, 1), (1, 2)),  # unigrams or bigrams
    "vect__norm": ("l1", "l2"),
    "clf__alpha": np.logspace(-6, 6, 13),
}

```

### Step 3: Hyperparameter Tuning

We use RandomizedSearchCV to explore the grid of hyperparameters and find the best combination of hyperparameters for the pipeline. In this case, we set n_iter=40 to limit the search space. We can increase n_iter to get a more informative analysis, but it will increase the computation time.

```python
from sklearn.model_selection import RandomizedSearchCV

random_search = RandomizedSearchCV(
    estimator=pipeline,
    param_distributions=parameter_grid,
    n_iter=40,
    random_state=0,
    n_jobs=2,
    verbose=1,
)

print("Performing grid search...")
print("Hyperparameters to be evaluated:")
pprint(parameter_grid)

random_search.fit(data_train.data, data_train.target)

test_accuracy = random_search.score(data_test.data, data_test.target)

```

### Step 4: Results Visualization

We can visualize the results of the hyperparameter tuning using plotly.express. We use a scatter plot to visualize the trade-off between scoring time and mean test score. We can also use parallel coordinates to further visualize the mean test score as a function of the tuned hyperparameters.

```python
import pandas as pd
import plotly.express as px
import math

def shorten_param(param_name):
    """Remove components' prefixes in param_name."""
    if "__" in param_name:
        return param_name.rsplit("__", 1)[1]
    return param_name

cv_results = pd.DataFrame(random_search.cv_results_)
cv_results = cv_results.rename(shorten_param, axis=1)

param_names = [shorten_param(name) for name in parameter_grid.keys()]
labels = {
    "mean_score_time": "CV Score time (s)",
    "mean_test_score": "CV score (accuracy)",
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
        "text": "trade-off between scoring time and mean test score",
        "y": 0.95,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

column_results = param_names + ["mean_test_score", "mean_score_time"]

transform_funcs = dict.fromkeys(column_results, lambda x: x)
# Using a logarithmic scale for alpha
transform_funcs["alpha"] = math.log10
# L1 norms are mapped to index 1, and L2 norms to index 2
transform_funcs["norm"] = lambda x: 2 if x == "l2" else 1
# Unigrams are mapped to index 1 and bigrams to index 2
transform_funcs["ngram_range"] = lambda x: x[1]

fig = px.parallel_coordinates(
    cv_results[column_results].apply(transform_funcs),
    color="mean_test_score",
    color_continuous_scale=px.colors.sequential.Viridis_r,
    labels=labels,
)
fig.update_layout(
    title={
        "text": "Parallel coordinates plot of text classifier pipeline",
        "y": 0.99,
        "x": 0.5,
        "xanchor": "center",
        "yanchor": "top",
    }
)

```

## Summary

In this lab, we demonstrated how to extract features from text data, build a pipeline, and evaluate the performance of the model using hyperparameter tuning. We used the 20newsgroups dataset to show how to use RandomizedSearchCV to find the best combination of hyperparameters for the pipeline and visualize the results using plotly.express.
