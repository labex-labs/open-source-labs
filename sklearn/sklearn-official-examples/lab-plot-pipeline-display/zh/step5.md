# 对带有分类器的管道进行网格搜索

在这一步中，我们将对带有分类器的管道进行网格搜索，并展示其可视化表示。

首先，我们导入必要的模块：

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

接下来，我们定义数值型和分类型特征的预处理步骤：

```python
numeric_preprocessor = Pipeline(
    steps=[
        ("均值插补", SimpleImputer(missing_values=np.nan, strategy="mean")),
        ("缩放器", StandardScaler()),
    ]
)

categorical_preprocessor = Pipeline(
    steps=[
        (
            "常量插补",
            SimpleImputer(fill_value="缺失", strategy="constant"),
        ),
        ("独热编码", OneHotEncoder(handle_unknown="ignore")),
    ]
)
```

然后，我们创建列变换器：

```python
preprocessor = ColumnTransformer(
    [
        ("分类型", categorical_preprocessor, ["州", "性别"]),
        ("数值型", numeric_preprocessor, ["年龄", "体重"]),
    ]
)
```

接下来，我们创建管道：

```python
pipe = Pipeline(
    steps=[("预处理", preprocessor), ("分类器", RandomForestClassifier())]
)
```

然后，我们定义网格搜索的参数网格：

```python
param_grid = {
    "分类器__n_estimators": [200, 500],
    "分类器__max_features": ["auto", "sqrt", "log2"],
    "分类器__max_depth": [4, 5, 6, 7, 8],
    "分类器__criterion": ["gini", "entropy"],
}
```

最后，我们创建网格搜索：

```python
grid_search = GridSearchCV(pipe, param_grid=param_grid, n_jobs=1)
```

并展示网格搜索的可视化表示：

```python
grid_search
```
