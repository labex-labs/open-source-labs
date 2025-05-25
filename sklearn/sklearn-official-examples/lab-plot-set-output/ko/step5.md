# 타이타닉 데이터셋 로드

다음으로, `compose.ColumnTransformer`와 이종 데이터를 사용하여 `set_output`를 보여주기 위해 타이타닉 데이터셋을 로드합니다.

```python
from sklearn.datasets import fetch_openml

X, y = fetch_openml(
    "titanic", version=1, as_frame=True, return_X_y=True, parser="pandas"
)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y)
```
