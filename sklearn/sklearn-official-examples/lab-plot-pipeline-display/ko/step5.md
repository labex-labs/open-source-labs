# 분류기를 포함한 파이프라인에 대한 그리드 검색 구축

이 단계에서는 분류기를 포함한 파이프라인에 대한 그리드 검색을 구축하고 시각적 표현을 보여줍니다.

먼저 필요한 모듈을 가져옵니다.

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
```

다음으로 숫자형 및 범주형 특징에 대한 전처리 단계를 정의합니다.

```python
numeric_preprocessor = Pipeline(
    steps=[
        ("imputation_mean", SimpleImputer(missing_values=np.nan, strategy="mean")),
        ("scaler", StandardScaler()),
    ]
)

categorical_preprocessor = Pipeline(
    steps=[
        (
            "imputation_constant",
            SimpleImputer(fill_value="missing", strategy="constant"),
        ),
        ("onehot", OneHotEncoder(handle_unknown="ignore")),
    ]
)
```

그런 다음 열 변환기를 생성합니다.

```python
preprocessor = ColumnTransformer(
    [
        ("categorical", categorical_preprocessor, ["state", "gender"]),
        ("numerical", numeric_preprocessor, ["age", "weight"]),
    ]
)
```

다음으로 파이프라인을 생성합니다.

```python
pipe = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", RandomForestClassifier())]
)
```

그런 다음 그리드 검색을 위한 매개변수 그리드를 정의합니다.

```python
param_grid = {
    "classifier__n_estimators": [200, 500],
    "classifier__max_features": ["auto", "sqrt", "log2"],
    "classifier__max_depth": [4, 5, 6, 7, 8],
    "classifier__criterion": ["gini", "entropy"],
}
```

마지막으로 그리드 검색을 생성합니다.

```python
grid_search = GridSearchCV(pipe, param_grid=param_grid, n_jobs=1)
```

그리드 검색의 시각적 표현을 보여줍니다.

```python
grid_search
```
