# Transformation des caractéristiques avec la forêt aléatoire et le gradient boosting

Maintenant, nous allons créer deux pipelines qui utiliseront l'imbrication ci-dessus comme étape de prétraitement. La transformation des caractéristiques se produira en appelant la méthode `apply`. Nous allons ensuite combiner la forêt aléatoire ou le gradient boosting avec une régression logistique dans un pipeline. Cependant, le pipeline dans scikit-learn attend un appel à `transform`. Par conséquent, nous avons encapsulé l'appel à `apply` dans un `FunctionTransformer`.

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
