# 데이터 타입별 컬럼 선택을 통한 ColumnTransformer 사용

이 단계에서는 데이터 타입별로 컬럼을 선택하여 `ColumnTransformer`를 사용합니다. `make_column_selector`를 사용하여 데이터 타입에 따라 컬럼을 선택합니다.

```python
from sklearn.compose import make_column_selector as selector

subset_feature = ["embarked", "sex", "pclass", "age", "fare"]
X_train, X_test = X_train[subset_feature], X_test[subset_feature]

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, selector(dtype_exclude="category")),
        ("cat", categorical_transformer, selector(dtype_include="category")),
    ]
)
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", LogisticRegression())]
)
```
