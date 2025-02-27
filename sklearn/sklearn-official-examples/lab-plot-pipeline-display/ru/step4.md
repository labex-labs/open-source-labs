# Построение сложного конвейера, объединяющего трансформер столбцов

В этом шаге мы построим сложный конвейер с трансформером столбцов и классификатором, и покажем его визуальное представление.

Во - первых, импортируем необходимые модули:

```python
import numpy as np
from sklearn.pipeline import make_pipeline
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LogisticRegression
```

Далее определяем этапы предварительной обработки для числовых и категориальных признаков:

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

Затем создаем трансформер столбцов:

```python
preprocessor = ColumnTransformer(
    [
        ("categorical", categorical_preprocessor, ["state", "gender"]),
        ("numerical", numeric_preprocessor, ["age", "weight"]),
    ]
)
```

Далее создаем конвейер:

```python
pipe = make_pipeline(preprocessor, LogisticRegression(max_iter=500))
```

Наконец, показываем визуальное представление конвейера:

```python
pipe
```
