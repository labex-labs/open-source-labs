# Digits 데이터셋 로드

scikit-learn 의 `load_digits` 함수를 사용하여 Digits 데이터셋을 로드합니다. 이 함수는 입력 데이터를 포함하는 `X_digits`와 대상 레이블을 포함하는 `y_digits` 두 개의 배열을 반환합니다.

```python
from sklearn import datasets

X_digits, y_digits = datasets.load_digits(return_X_y=True)
```
