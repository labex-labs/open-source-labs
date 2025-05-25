# 데이터를 학습 및 테스트 세트로 분할

데이터를 학습 세트와 테스트 세트로 50% 씩 분할할 것입니다.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
```
