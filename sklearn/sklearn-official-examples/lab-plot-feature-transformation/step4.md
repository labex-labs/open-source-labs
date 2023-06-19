# Transforming Features with Random Forest and Gradient Boosting

Now, we will create two pipelines that will use the above embedding as a preprocessing stage. The feature transformation will happen by calling the method `apply`. We will then pipeline random forest or gradient boosting with a logistic regression. However, the pipeline in scikit-learn expects a call to `transform`. Therefore, we wrapped the call to `apply` within a `FunctionTransformer`.

```python
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import OneHotEncoder

def rf_apply(X, model):
    return model.apply(X)

rf_leaves_yielder = FunctionTransformer(rf_apply, kw_args={"model": random_forest})

rf_model = make_pipeline(
    rf_leaves_yielder,
    OneHotEncoder(handle_unknown="ignore"),
    LogisticRegression(max_iter=1000),
)
rf_model.fit(X_train_linear, y_train_linear)

def gbdt_apply(X, model):
    return model.apply(X)[:, :, 0]

gbdt_leaves_yielder = FunctionTransformer(
    gbdt_apply, kw_args={"model": gradient_boosting}
)

gbdt_model = make_pipeline(
    gbdt_leaves_yielder,
    OneHotEncoder(handle_unknown="ignore"),
    LogisticRegression(max_iter=1000),
)
gbdt_model.fit(X_train_linear, y_train_linear)
```


