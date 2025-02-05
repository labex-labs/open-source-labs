# 构建一个链接列变换器的复杂管道

在这一步中，我们将构建一个带有列变换器和分类器的复杂管道，并展示其可视化表示。

首先，我们导入必要的模块：

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
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
pipe = make_pipeline(preprocessor, LogisticRegression(max_iter=500))
```

最后，我们展示管道的可视化表示：

```python
pipe
```
