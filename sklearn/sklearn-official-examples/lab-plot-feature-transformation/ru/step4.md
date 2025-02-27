# Преобразование признаков с использованием Random Forest и Gradient Boosting

Теперь мы создадим два конвейера, которые будут использовать вышеописанное встраивание на этапе предварительной обработки. Преобразование признаков произойдет при вызове метода `apply`. Затем мы создадим конвейер, включающий в себя Random Forest или Gradient Boosting, а также логистическую регрессию. Однако, конвейер в scikit - learn ожидает вызов метода `transform`. Поэтому мы обернули вызов `apply` в `FunctionTransformer`.

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
