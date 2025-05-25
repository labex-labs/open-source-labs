# Transformando Recursos com Random Forest e Gradient Boosting

Agora, criaremos dois pipelines que usarão a incorporação acima como uma etapa de pré-processamento. A transformação de recursos ocorrerá chamando o método `apply`. Em seguida, concatenaremos random forest ou gradient boosting com uma regressão logística. No entanto, o pipeline no scikit-learn espera uma chamada para `transform`. Portanto, envolvemos a chamada para `apply` dentro de um `FunctionTransformer`.

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
