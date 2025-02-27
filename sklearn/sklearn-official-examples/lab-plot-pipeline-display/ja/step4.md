# 列変換器を連鎖させた複雑なパイプラインの構築

このステップでは、列変換器と分類器を備えた複雑なパイプラインを構築し、その視覚的表現を表示します。

まず、必要なモジュールをインポートします。

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
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
pipe = make_pipeline(preprocessor, LogisticRegression(max_iter=500))
```

最後に、パイプラインの視覚的表現を表示します。

```python
pipe
```
