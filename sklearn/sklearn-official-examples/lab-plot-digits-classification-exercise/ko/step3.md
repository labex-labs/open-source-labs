# 데이터셋을 학습 및 테스트 세트로 분할

다음으로, scikit-learn 의 `train_test_split` 함수를 사용하여 데이터셋을 학습 및 테스트 세트로 분할합니다. 학습에는 데이터의 90%, 테스트에는 10% 를 사용합니다.

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X_digits, y_digits, test_size=0.1, random_state=42)
```
