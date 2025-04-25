# 使用随机森林和梯度提升进行特征转换

现在，我们将创建两个管道，它们将使用上述嵌入作为预处理阶段。特征转换将通过调用`apply`方法来实现。然后，我们将随机森林或梯度提升与逻辑回归进行管道连接。然而，scikit-learn 中的管道期望调用`transform`。因此，我们将对`apply`的调用包装在一个`FunctionTransformer`中。

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
