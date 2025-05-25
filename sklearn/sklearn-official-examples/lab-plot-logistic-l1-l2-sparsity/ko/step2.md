# 데이터셋 로드

`datasets.load_digits(return_X_y=True)`를 사용하여 숫자 데이터셋을 로드합니다. 또한 `StandardScaler().fit_transform(X)`를 사용하여 데이터를 표준화합니다. 타겟 변수는 이진 변수로, 0-4 는 0 으로, 5-9 는 1 로 분류됩니다.

```python
X, y = datasets.load_digits(return_X_y=True)
X = StandardScaler().fit_transform(X)
y = (y > 4).astype(int)
```
