# ランダムフォレストと勾配ブースティングによる特徴量の変換

ここで、上記の埋め込みを前処理段階として使用する2つのパイプラインを作成します。特徴量の変換は、`apply`メソッドを呼び出すことによって行われます。その後、ロジスティック回帰によるランダムフォレストまたは勾配ブースティングをパイプライン化します。ただし、scikit - learnのパイプラインは`transform`への呼び出しを期待しています。したがって、`apply`への呼び出しを`FunctionTransformer`内にラップしました。

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
