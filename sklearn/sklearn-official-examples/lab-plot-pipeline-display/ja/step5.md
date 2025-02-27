# 分類器付きパイプラインに対するグリッドサーチの構築

このステップでは、分類器付きパイプラインに対するグリッドサーチを構築し、その視覚的表現を表示します。

まず、必要なモジュールをインポートします。

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

次に、数値型とカテゴリ型の特徴量に対する前処理ステップを定義します。

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

そして、列変換器を作成します。

```python
preprocessor = ColumnTransformer(
    [
        ("categorical", categorical_preprocessor, ["state", "gender"]),
        ("numerical", numeric_preprocessor, ["age", "weight"]),
    ]
)
```

次に、パイプラインを作成します。

```python
pipe = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier", RandomForestClassifier())]
)
```

その後、グリッドサーチ用のパラメータグリッドを定義します。

```python
param_grid = {
    "classifier__n_estimators": [200, 500],
    "classifier__max_features": ["auto", "sqrt", "log2"],
    "classifier__max_depth": [4, 5, 6, 7, 8],
    "classifier__criterion": ["gini", "entropy"],
}
```

最後に、グリッドサーチを作成します。

```python
grid_search = GridSearchCV(pipe, param_grid=param_grid, n_jobs=1)
```

そして、グリッドサーチの視覚的表現を表示します。

```python
grid_search
```
