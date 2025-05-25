# Iris 데이터셋 로드

먼저, `set_output` API 를 보여주기 위해 Iris 데이터셋을 DataFrame 으로 로드합니다.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

X, y = load_iris(as_frame=True, return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=0)
X_train.head()
```
