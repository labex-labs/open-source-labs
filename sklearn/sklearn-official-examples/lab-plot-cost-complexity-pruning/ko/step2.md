# 데이터 분할

데이터를 학습 데이터셋과 테스트 데이터셋으로 분할합니다.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
```
