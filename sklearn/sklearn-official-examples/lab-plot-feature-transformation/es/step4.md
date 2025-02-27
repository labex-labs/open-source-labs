# Transformando características con Random Forest y Gradient Boosting

Ahora, crearemos dos tuberías que utilizarán la incrustación anterior como etapa de preprocesamiento. La transformación de características se realizará llamando al método `apply`. Luego, encadenaremos Random Forest o Gradient Boosting con una regresión logística. Sin embargo, la tubería en scikit-learn espera una llamada a `transform`. Por lo tanto, envolvemos la llamada a `apply` dentro de un `FunctionTransformer`.

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
