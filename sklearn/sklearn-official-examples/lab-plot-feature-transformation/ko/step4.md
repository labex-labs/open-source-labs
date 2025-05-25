# 랜덤 포레스트와 그래디언트 부스팅을 이용한 특징 변환

이제 위의 임베딩을 전처리 단계로 사용하는 두 개의 파이프라인을 생성합니다. 특징 변환은 `apply` 메서드를 호출하여 수행됩니다. 그런 다음 랜덤 포레스트 또는 그래디언트 부스팅을 로지스틱 회귀와 파이프라인으로 연결합니다. 하지만 scikit-learn 의 파이프라인은 `transform` 호출을 기대하므로 `apply` 호출을 `FunctionTransformer`로 감쌌습니다.

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
