# Loading Data from OpenML

First, we load the wine reviews dataset using `fetch_openml` function from scikit-learn.datasets module. We will only use a subset of numerical and categorical features in the data. We will use the following subset of numerical and categorical features in the data: `numerical_features = ["price"]` and `categorical_features = ["country", "province", "region_1", "region_2", "variety", "winery"]`.


