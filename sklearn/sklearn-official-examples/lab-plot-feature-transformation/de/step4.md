# Transforming Features with Random Forest and Gradient Boosting

Jetzt werden wir zwei Pipelines erstellen, die die obige Embedding als Vorverarbeitungsschritt verwenden. Die Feature-Transformation wird durch Aufruf der Methode `apply` erfolgen. Anschließend werden wir Random Forest oder Gradient Boosting mit einer logistischen Regression in eine Pipeline packen. Allerdings erwartet die Pipeline in scikit-learn einen Aufruf von `transform`. Daher haben wir den Aufruf von `apply` in einem `FunctionTransformer` eingeschlossen.

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
